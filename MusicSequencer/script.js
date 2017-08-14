// plays sounds
// beats
// bpm
// 8 count

// globals globals globals
ratio = 5;
// globals globals globals

// play a note
audio_context = new AudioContext();

pulse1_oscillator = audio_context.createOscillator();
pulse1_oscillator.type = 'square';
pulse1 = audio_context.createGain();
pulse1.gain.value = 0;
pulse1_oscillator.connect(pulse1);

pulse2_oscillator = audio_context.createOscillator();
pulse2_oscillator.type = 'square';
pulse2 = audio_context.createGain();
pulse2.gain.value = 0;
pulse2_oscillator.connect(pulse2);

triangle_oscillator = audio_context.createOscillator();
triangle_oscillator.type = 'sawtooth';
triangle = audio_context.createGain();
triangle.gain.value = 0;
triangle_oscillator.connect(triangle);

var bufferSize = 4096;
var noise_generator = (function() {
    var lastOut = 0.0;
    var node = audio_context.createScriptProcessor(bufferSize, 1, 1);
    node.onaudioprocess = function(e) {
        var output = e.outputBuffer.getChannelData(0);
        for (var i = 0; i < bufferSize; i++) {
            var white = Math.random() * 2 - 1;
            output[i] = (lastOut + (0.02 * white)) / 1.02;
            lastOut = output[i];
            output[i] *= 3.5; // (roughly) compensate for gain
        }
    }
    return node;
})();
noise = audio_context.createGain();
noise.gain.value = 0;
noise_generator.connect(noise);

var high_pass_90_filter = audio_context.createBiquadFilter();
high_pass_90_filter.type = 'highpass';
high_pass_90_filter.frequency.value = 90;

var high_pass_440_filter = audio_context.createBiquadFilter();
high_pass_440_filter.type = 'highpass';
high_pass_440_filter.frequency.value = 440;

var low_pass_14000_filter = audio_context.createBiquadFilter();
low_pass_14000_filter.type = 'lowpass';
low_pass_14000_filter.frequency.value = 14000;

low_pass_14000_filter.connect(audio_context.destination);
high_pass_440_filter.connect(low_pass_14000_filter);
high_pass_90_filter.connect(high_pass_440_filter);
pulse1.connect(high_pass_90_filter);
pulse2.connect(high_pass_90_filter);
triangle.connect(high_pass_90_filter);
noise.connect(high_pass_90_filter);

pulse1_oscillator.start();
pulse2_oscillator.start();
triangle_oscillator.start();
// noise.start();

//document.addEventListener("keydown", function (e) {
//  if (e.keyCode == 38) {
//    ratio += 1;
//    reset_oscillator2_value();
//    e.preventDefault();
//  } else if (e.keyCode == 40) {
//    ratio -= 1;
//    reset_oscillator2_value();
//    e.preventDefault();
//  }
//})

// Config svgo segura para los SVG animados de Dr. Cuack.
// Conserva IDs, <style>, @keyframes y @media(prefers-reduced-motion) —los
// necesita el CSS de animación— y optimiza a fondo el trazo (donde está el peso).
export default {
  multipass: true,
  plugins: [
    { name: 'preset-default', params: { overrides: {
      cleanupIds: false,
      minifyStyles: false,
      inlineStyles: false,
      removeViewBox: false,
      removeHiddenElems: false,
    }}},
  ],
};

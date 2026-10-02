# LOOPS Research Group website

Website of the LOOPS research group (Learning and Optimisation Of Process Systems), UCL Department of Chemical Engineering, led by Dr Paulina Quintanilla.

Built with [Hugo](https://gohugo.io) and the [Hugo Blox](https://docs.hugoblox.com/) research group theme, and deployed with Netlify.

## Editing

- `content/authors/` – team profiles (one folder per person, with `avatar.jpg`)
- `content/people/index.md` – Team page sections, Alumni and Join Us
- `content/post/` – news posts
- `content/publication/` – publications
- `content/research/index.md` – Research page
- `assets/scss/custom.scss` – custom styles

In a publication's `authors` list, use a group member's profile folder name (e.g. `paulina-quintanilla`) so the name links to their profile. The short name shown in citations comes from `linkTitle` in their profile.

## Research figures

The labelled figures on the Research page are generated from the drawings in `tools/research-figures/sources/`:

```bash
python3 tools/research-figures/label_figures.py
```

## Preview locally

```bash
hugo server
```

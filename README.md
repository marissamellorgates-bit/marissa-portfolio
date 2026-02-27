# Marissa Gates — Portfolio Site

## Deploy to Vercel

### Option A: Drag & Drop (Easiest)
1. Go to [vercel.com](https://vercel.com) and sign in (or create account with GitHub)
2. On the dashboard, look for "Add New Project"
3. Choose "Upload" or drag the entire `portfolio-deploy` folder onto the page
4. Vercel will auto-detect the static site and deploy it
5. You'll get a URL like `portfolio-deploy.vercel.app` — you can customize this in settings

### Option B: GitHub + Vercel (Better for Updates)
1. Create a new repo on GitHub called `portfolio`
2. Push the contents of this folder to the repo
3. In Vercel, click "Add New Project" → "Import Git Repository"
4. Select your `portfolio` repo
5. Vercel auto-deploys on every push to main

### Customizing
- **Email**: Search for `marissa@example.com` and replace with real email
- **LinkedIn**: Search for `class="contact-link"` and update the LinkedIn href
- **Resume**: Upload resume PDF to /public and link it
- **Photos**: Add project screenshots to /public and reference in img tags
- **Storyline embed**: After publishing Storyline as web, upload to /public/storyline/ and replace the placeholder with an iframe

### Adding the Storyline Embed
1. In Storyline, publish as "Web" (not LMS)
2. Upload the published folder to `/public/storyline/`
3. Replace the embed-placeholder div with:
   ```html
   <iframe src="/storyline/story.html" width="100%" height="480" frameborder="0"></iframe>
   ```

### Custom Domain (Optional)
In Vercel dashboard → Settings → Domains → Add your custom domain

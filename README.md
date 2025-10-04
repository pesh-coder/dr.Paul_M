# Dr. Paul Mwambu Portfolio Website

A professional portfolio and showcase platform for Dr. Paul Mwambu—a renowned leader in Ugandan agriculture and Prime Minister of the Bamasaba cultural institution—built with Django & Tailwind CSS.

## About Dr. Paul Mwambu

Dr. Paul Mwambu is a leading Ugandan agricultural expert and administrator, recognized nationally and internationally for his work in crop certification, sustainable agriculture, and rural development.

### Current Roles
- Commissioner for Crop Inspection & Certification, Ministry of Agriculture, Animal Industry, and Fisheries (MAAIF), Uganda
- Prime Minister of Inzu Ya Masaba (appointed Dec 2024), leading cultural, social, and agricultural initiatives for the Bamasaba community

### Education
- PhD in Management Studies (Uganda Management Institute)
- Studies in Botany, Zoology, Public Administration, and Pesticide Risk Management

### Impact & Achievements
- Over 30 years' experience in agriculture, policy, research, and rural development
- Recognized with Uganda's Diamond Jubilee Medal for outstanding agricultural service (May 2024)
- Led major programs supporting farming modernization, food security, and climate-smart agriculture
- Championed national and international collaborations with World Bank, UNDP, and others

## Features

### Core Components
- **Home/Landing Page** - Hero section, impact highlights, featured content
- **About/Biography** - Detailed professional background and achievements
- **Projects/Initiatives** - Showcase of key programs and initiatives
- **Awards & Honors** - Recognition and achievements
- **Gallery** - Responsive image gallery with lightbox functionality
- **Blog/Updates** - Latest insights and updates
- **Contact** - Contact form and information
- **Testimonials** - Feedback from colleagues and partners

### Technical Features
- **Django Framework** - Robust backend with admin interface
- **Tailwind CSS** - Modern, responsive design
- **Wagtail CMS** - Content management system
- **Django REST Framework** - API endpoints
- **SEO Optimization** - Meta tags and Open Graph support
- **Responsive Design** - Mobile-first approach
- **Accessibility** - WCAG compliant
- **Docker Support** - Containerization ready

## Installation

### Prerequisites
- Python 3.11+
- Node.js 18+
- npm or yarn

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd dr_paulM
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Node.js dependencies**
   ```bash
   npm install
   ```

5. **Environment configuration**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

6. **Database setup**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

7. **Build CSS**
   ```bash
   npm run build-css-prod
   ```

8. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

9. **Run development server**
   ```bash
   python manage.py runserver
   ```

## Usage

### Admin Interface
Access the Django admin at `/admin/` to manage:
- Biography information
- Projects and initiatives
- Awards and recognition
- Gallery images
- Blog posts
- Testimonials
- Contact messages
- Site settings

### Content Management
- Use Wagtail CMS at `/cms/` for advanced content management
- API endpoints available at `/api/` for programmatic access

### Customization
- Modify `static/css/input.css` for custom styles
- Update `tailwind.config.js` for theme customization
- Edit templates in `templates/portfolio/` for layout changes

## Deployment

### Docker Deployment
```bash
docker build -t dr-paul-mwambu .
docker run -p 8000:8000 dr-paul-mwambu
```

### Production Settings
1. Set `DEBUG=False` in environment variables
2. Configure proper database (PostgreSQL recommended)
3. Set up static file serving
4. Configure email settings
5. Set up SSL/HTTPS

### Recommended Hosting
- Render
- Vercel
- Heroku
- DigitalOcean
- AWS

## API Endpoints

The application provides REST API endpoints:

- `/api/projects/` - Project listings and details
- `/api/awards/` - Awards and recognition
- `/api/gallery/` - Gallery images
- `/api/blog/` - Blog posts
- `/api/testimonials/` - Testimonials
- `/api/bio/` - Biography information

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Contact

For questions or collaboration opportunities, please contact Dr. Paul Mwambu through the contact form on the website.

## Acknowledgments

- Built with Django and Tailwind CSS
- Icons from Heroicons
- Images optimized for web performance
- Accessibility features following WCAG guidelines
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta
from portfolio.models import (
    Bio, Project, Award, GalleryImage, BlogPost, 
    Testimonial, Message, SiteSettings
)


class Command(BaseCommand):
    help = 'Populate the database with sample data for Dr. Paul Mwambu'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create Site Settings
        site_settings, created = SiteSettings.objects.get_or_create(
            defaults={
                'site_title': 'Dr. Paul Mwambu - Agricultural Leader',
                'site_description': 'Professional portfolio of Dr. Paul Mwambu, Commissioner for Crop Inspection & Certification, Uganda',
                'contact_email': 'contact@drpaulmwambu.com',
                'contact_phone': '+256 700 000 000',
                'address': 'Ministry of Agriculture, Animal Industry, and Fisheries, Kampala, Uganda',
                'social_linkedin': 'https://linkedin.com/in/drpaulmwambu',
                'social_twitter': 'https://twitter.com/drpaulmwambu',
                'social_facebook': 'https://facebook.com/drpaulmwambu',
            }
        )
        if created:
            self.stdout.write('✓ Created site settings')

        # Create Biography
        bio, created = Bio.objects.get_or_create(
            defaults={
                'name': 'Dr. Paul Mwambu',
                'title': 'Commissioner for Crop Inspection & Certification',
                'organization': 'Ministry of Agriculture, Animal Industry, and Fisheries (MAAIF), Uganda',
                'bio': '''Dr. Paul Mwambu is a leading Ugandan agricultural expert and administrator, recognized nationally and internationally for his work in crop certification, sustainable agriculture, and rural development.

With over 30 years of experience in agriculture, policy, research, and rural development, Dr. Mwambu has been instrumental in transforming Uganda's agricultural sector. He currently serves as the Commissioner for Crop Inspection & Certification at the Ministry of Agriculture, Animal Industry, and Fisheries (MAAIF), Uganda, and was recently appointed as Prime Minister of Inzu Ya Masaba in December 2024.

Dr. Mwambu holds a PhD in Management Studies from the Uganda Management Institute, with additional studies in Botany, Zoology, Public Administration, and Pesticide Risk Management. His extensive background has enabled him to lead major programs supporting farming modernization, food security, and climate-smart agriculture.

In recognition of his outstanding contributions, Dr. Mwambu was awarded Uganda's Diamond Jubilee Medal in May 2024 for exceptional agricultural service. He has championed national and international collaborations with organizations such as the World Bank and UNDP, significantly impacting rural communities and agricultural practices across Uganda.

His vision centers on promoting sustainable, commercial agriculture that elevates Uganda's crop export standards while empowering rural youth and farmers to succeed in modern farming practices.''',
                'email': 'contact@drpaulmwambu.com',
                'phone': '+256 700 000 000',
                'linkedin': 'https://linkedin.com/in/drpaulmwambu',
                'twitter': 'https://twitter.com/drpaulmwambu',
            }
        )
        if created:
            self.stdout.write('✓ Created biography')

        # Create Projects
        projects_data = [
            {
                'title': 'National Crop Certification Program',
                'description': 'A comprehensive program to establish and maintain quality standards for agricultural exports from Uganda.',
                'detailed_description': 'This initiative has transformed Uganda\'s agricultural export capabilities by implementing rigorous quality assurance protocols. The program covers over 50 crop varieties and has enabled thousands of farmers to access international markets.',
                'start_date': date(2020, 1, 1),
                'status': 'ongoing',
                'featured': True,
            },
            {
                'title': 'Climate-Smart Agriculture Initiative',
                'description': 'Promoting sustainable farming practices that adapt to climate change while improving productivity.',
                'detailed_description': 'This project focuses on introducing drought-resistant crops, water conservation techniques, and sustainable farming methods to help farmers adapt to changing climate conditions.',
                'start_date': date(2021, 6, 1),
                'status': 'ongoing',
                'featured': True,
            },
            {
                'title': 'Rural Youth Empowerment Program',
                'description': 'Training and supporting young people in modern agricultural practices and entrepreneurship.',
                'detailed_description': 'A comprehensive program that provides technical training, access to credit, and mentorship opportunities for young people interested in agriculture and agribusiness.',
                'start_date': date(2019, 3, 1),
                'end_date': date(2023, 12, 31),
                'status': 'completed',
                'featured': True,
            },
            {
                'title': 'Export Market Development',
                'description': 'Expanding Uganda\'s agricultural exports to new international markets.',
                'detailed_description': 'This initiative has successfully opened new export markets in Europe, Asia, and the Middle East, significantly increasing Uganda\'s agricultural export revenue.',
                'start_date': date(2018, 1, 1),
                'status': 'ongoing',
                'featured': False,
            },
        ]

        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f'✓ Created project: {project.title}')

        # Create Awards
        awards_data = [
            {
                'name': 'Diamond Jubilee Medal',
                'organization': 'Government of Uganda',
                'date': date(2024, 5, 1),
                'description': 'Awarded for outstanding agricultural service and contributions to rural development in Uganda.',
                'category': 'service',
                'featured': True,
            },
            {
                'name': 'Agricultural Excellence Award',
                'organization': 'Uganda National Farmers Federation',
                'date': date(2023, 12, 1),
                'description': 'Recognition for exceptional leadership in agricultural policy and farmer support programs.',
                'category': 'leadership',
                'featured': True,
            },
            {
                'name': 'International Collaboration Award',
                'organization': 'World Bank',
                'date': date(2023, 6, 1),
                'description': 'Awarded for outstanding contributions to international agricultural development projects.',
                'category': 'international',
                'featured': True,
            },
            {
                'name': 'Research Innovation Award',
                'organization': 'National Agricultural Research Organization',
                'date': date(2022, 9, 1),
                'description': 'Recognition for innovative research in crop certification and quality assurance.',
                'category': 'research',
                'featured': False,
            },
        ]

        for award_data in awards_data:
            award, created = Award.objects.get_or_create(
                name=award_data['name'],
                organization=award_data['organization'],
                defaults=award_data
            )
            if created:
                self.stdout.write(f'✓ Created award: {award.name}')

        # Create Blog Posts
        blog_posts_data = [
            {
                'title': 'The Future of Sustainable Agriculture in Uganda',
                'slug': 'future-sustainable-agriculture-uganda',
                'excerpt': 'Exploring innovative approaches to sustainable farming that can transform Uganda\'s agricultural sector.',
                'body': '''Sustainable agriculture is not just a trend; it's a necessity for Uganda's future. As we face the challenges of climate change and growing population demands, we must adopt farming practices that protect our environment while ensuring food security.

The key to sustainable agriculture lies in three pillars: environmental health, economic profitability, and social equity. In Uganda, we have the unique opportunity to implement these principles from the ground up, learning from both traditional knowledge and modern innovations.

One of the most promising approaches is climate-smart agriculture, which helps farmers adapt to changing weather patterns while reducing greenhouse gas emissions. This includes practices like conservation agriculture, agroforestry, and integrated pest management.

Another critical aspect is empowering smallholder farmers with the knowledge and resources they need to succeed. Through our rural development programs, we're seeing remarkable transformations in communities that have adopted sustainable practices.

The future of agriculture in Uganda depends on our ability to balance productivity with sustainability. By investing in research, education, and infrastructure, we can create a thriving agricultural sector that benefits both farmers and the environment.''',
                'author': 'Dr. Paul Mwambu',
                'published': True,
                'featured': True,
                'tags': 'sustainable agriculture, climate change, farming, Uganda',
            },
            {
                'title': 'Crop Certification: Building Trust in Global Markets',
                'slug': 'crop-certification-building-trust-global-markets',
                'excerpt': 'How proper crop certification processes are essential for accessing international markets and building consumer confidence.',
                'body': '''In today's globalized world, crop certification has become more than just a regulatory requirement—it's a gateway to international markets and a symbol of quality and trust.

The certification process ensures that agricultural products meet specific standards for quality, safety, and sustainability. For Ugandan farmers, this means access to premium markets and better prices for their produce.

Our National Crop Certification Program has been instrumental in helping thousands of farmers meet international standards. The program covers everything from seed selection and farming practices to post-harvest handling and packaging.

One of the key benefits of certification is the premium prices that certified products command in international markets. This not only improves farmers' incomes but also encourages the adoption of better farming practices.

However, certification is not without its challenges. The process can be complex and costly for smallholder farmers. That's why we've developed support programs that help farmers navigate the certification process and access the necessary resources.

Looking ahead, we're working on expanding our certification programs to cover more crop varieties and developing partnerships with international certification bodies to ensure our standards meet global requirements.''',
                'author': 'Dr. Paul Mwambu',
                'published': True,
                'featured': True,
                'tags': 'certification, exports, quality, international markets',
            },
            {
                'title': 'Empowering Rural Youth Through Agriculture',
                'slug': 'empowering-rural-youth-through-agriculture',
                'excerpt': 'The importance of engaging young people in agriculture and providing them with the tools they need to succeed.',
                'body': '''Agriculture has often been seen as a traditional sector with limited opportunities for young people. However, this perception is changing rapidly as we recognize the immense potential that agriculture holds for youth empowerment and economic development.

Our Rural Youth Empowerment Program has been a game-changer for many young people in Uganda. By providing training in modern agricultural techniques, business skills, and access to credit, we're helping young people build successful careers in agriculture.

The program focuses on three key areas: technical training, entrepreneurship development, and market access. Participants learn about modern farming techniques, post-harvest handling, and value addition, while also developing business and marketing skills.

One of the most exciting aspects of the program is the emphasis on technology and innovation. Young people are naturally drawn to technology, and we're leveraging this to introduce digital tools and precision agriculture techniques.

The results have been remarkable. Many program graduates have started successful agribusinesses, creating jobs and contributing to their communities' economic development. Others have become agricultural extension workers, helping to spread knowledge and best practices.

As we look to the future, we're expanding the program to reach more young people and incorporating new technologies like mobile applications, drone technology, and data analytics to make agriculture more attractive and profitable for the next generation.''',
                'author': 'Dr. Paul Mwambu',
                'published': True,
                'featured': False,
                'tags': 'youth, empowerment, agriculture, entrepreneurship',
            },
        ]

        for post_data in blog_posts_data:
            post, created = BlogPost.objects.get_or_create(
                slug=post_data['slug'],
                defaults=post_data
            )
            if created:
                self.stdout.write(f'✓ Created blog post: {post.title}')

        # Create Testimonials
        testimonials_data = [
            {
                'author': 'Dr. Jane Mukasa',
                'position': 'Director of Agricultural Research',
                'organization': 'National Agricultural Research Organization (NARO)',
                'quote': 'Dr. Paul Mwambu\'s leadership in crop certification has transformed Uganda\'s agricultural export standards. His dedication to quality assurance and farmer empowerment is truly commendable.',
                'featured': True,
            },
            {
                'author': 'Robert Kato',
                'position': 'Chairman',
                'organization': 'Uganda National Farmers Federation',
                'quote': 'Working with Dr. Paul Mwambu has been instrumental in advancing our farming practices. His vision for sustainable agriculture aligns perfectly with our goals for rural development.',
                'featured': True,
            },
            {
                'author': 'Sarah Mbabazi',
                'position': 'Program Manager',
                'organization': 'World Bank Uganda',
                'quote': 'Dr. Paul Mwambu\'s expertise in agricultural policy and implementation has been crucial to the success of our rural development programs in Uganda.',
                'featured': True,
            },
            {
                'author': 'Dr. David Nsubuga',
                'position': 'Professor of Agriculture',
                'organization': 'Makerere University',
                'quote': 'Dr. Paul Mwambu\'s contributions to agricultural research and policy development have significantly impacted Uganda\'s food security and rural livelihoods.',
                'featured': False,
            },
        ]

        for testimonial_data in testimonials_data:
            testimonial, created = Testimonial.objects.get_or_create(
                author=testimonial_data['author'],
                organization=testimonial_data['organization'],
                defaults=testimonial_data
            )
            if created:
                self.stdout.write(f'✓ Created testimonial: {testimonial.author}')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data!')
        )

import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Lines 567-624: the testimonial-slider div and all cards
# Replace with a proper carousel with dot navigation
# Line 567 is <div class="testimonial-slider"> (0-indexed: 566)
# Line 624 is </div> closing testimonial-slider (0-indexed: 623)
# Line 625 is </section> (0-indexed: 624)

new_slider = '''      <div class="testimonial-carousel-wrapper" style="position: relative; overflow: hidden; padding: 0 0 var(--space-8) 0;">
        <div class="testimonial-track" id="testimonialTrack" style="display: flex; transition: transform 0.5s ease; gap: 0;">
          <!-- Card 1 -->
          <div class="testimonial-slide" style="min-width: 100%; display: flex; gap: 2rem; padding: 0 5%;">
            <div class="testimonial-card" style="flex: 1;"><div class="testimonial-avatar">PS</div><p>"Working with Cling Info Tech was a game-changer for our business. Their expertise and dedication helped us achieve remarkable results. I highly recommend them to anyone looking for top-notch service."</p><div class="author-name">Praveen Shetty</div></div>
            <div class="testimonial-card" style="flex: 1;"><div class="testimonial-avatar" style="background: var(--color-accent);">SA</div><p>"Cling Info Tech's professionalism and efficiency surpassed our expectations, understanding our needs exceptionally well. Rarely do we find such a reliable partner in today's market."</p><div class="author-name">Swatee Agrawal</div><div class="author-role">Founder - Piaah.com</div></div>
            <div class="testimonial-card" style="flex: 1;"><div class="testimonial-avatar" style="background: var(--color-dark);">ET</div><p>"Choosing Cling Info Tech was one of the best decisions we made. Their team's creativity and strategic approach transformed our vision into reality."</p><div class="author-name">Elizabeth Jean Thomas</div><div class="author-role">Founder - Speech Ally</div></div>
          </div>
          <!-- Card 2 -->
          <div class="testimonial-slide" style="min-width: 100%; display: flex; gap: 2rem; padding: 0 5%;">
            <div class="testimonial-card" style="flex: 1;"><div class="testimonial-avatar">ST</div><p>"Working with Cling Info Tech was an absolute pleasure throughout. Finding a partner who truly understands your needs is invaluable, and Cling Info Tech excels exceptionally in this regard."</p><div class="author-name">Shams Tabrez</div><div class="author-role">Director - Litmus Ink</div></div>
            <div class="testimonial-card" style="flex: 1;"><div class="testimonial-avatar" style="background: var(--color-accent);">AK</div><p>"Cling Info Tech exceeded all our expectations with their professionalism and efficiency. They consistently went above and beyond to deliver outstanding results."</p><div class="author-name">Ashish Kumar</div><div class="author-role">Director - Vibgyorweb</div></div>
            <div class="testimonial-card" style="flex: 1;"><div class="testimonial-avatar" style="background: var(--color-dark);">AB</div><p>"Working with Cling Info Tech was an absolute pleasure throughout. Finding a partner who truly understands your needs is invaluable."</p><div class="author-name">Aurko Bhattacharya</div><div class="author-role">Co-founder - ePayLater</div></div>
          </div>
          <!-- Card 3 -->
          <div class="testimonial-slide" style="min-width: 100%; display: flex; gap: 2rem; padding: 0 5%;">
            <div class="testimonial-card" style="flex: 1;"><div class="testimonial-avatar">AS</div><p>"Choosing Cling Info Tech was one of the best decisions we made. Their team's creativity transformed our vision into reality."</p><div class="author-name">Ankit Solanki</div></div>
            <div class="testimonial-card" style="flex: 1;"><div class="testimonial-avatar" style="background: var(--color-accent);">SS</div><p>"Rarely do we find such a reliable partner in today's market. Their dedication sets them apart."</p><div class="author-name">Shubhanshu Srivastava</div></div>
            <div class="testimonial-card" style="flex: 1;"><div class="testimonial-avatar" style="background: var(--color-dark);">GS</div><p>"Cling Info Tech excels exceptionally in understanding needs in today's fiercely competitive market."</p><div class="author-name">Gourav Singh</div><div class="author-role">CFO - Webisdom</div></div>
          </div>
        </div>

        <!-- Dot Navigation -->
        <div style="display: flex; justify-content: center; gap: 10px; margin-top: var(--space-6);">
          <button onclick="goToSlide(0)" class="dot-btn" id="dot-0" style="width: 12px; height: 12px; border-radius: 50%; border: 2px solid white; background: white; cursor: pointer; padding: 0; transition: all 0.3s;"></button>
          <button onclick="goToSlide(1)" class="dot-btn" id="dot-1" style="width: 12px; height: 12px; border-radius: 50%; border: 2px solid white; background: transparent; cursor: pointer; padding: 0; transition: all 0.3s;"></button>
          <button onclick="goToSlide(2)" class="dot-btn" id="dot-2" style="width: 12px; height: 12px; border-radius: 50%; border: 2px solid white; background: transparent; cursor: pointer; padding: 0; transition: all 0.3s;"></button>
        </div>
      </div>

      <script>
        let currentSlide = 0;
        const totalSlides = 3;
        function goToSlide(index) {
          currentSlide = index;
          document.getElementById('testimonialTrack').style.transform = 'translateX(-' + (index * 100) + '%)';
          document.querySelectorAll('.dot-btn').forEach((d, i) => {
            d.style.background = i === index ? 'white' : 'transparent';
          });
        }
        // Auto-play
        setInterval(() => { goToSlide((currentSlide + 1) % totalSlides); }, 5000);
      </script>
'''

new_lines = lines[:566]  # keep up to line 566 (0-indexed 565 = the blank line after </div>)
new_lines.append(new_slider)
new_lines.extend(lines[624:])  # skip old slider (lines 567-624), resume from </section>

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Done!")

with open('references.html', 'r') as f:
    html = f.read()

jennifer_card = '''
                    <!-- Jennifer Kuehn - Colleague -->
                    <div class="ref-card-wrapper" data-category="colleague">
                        <div class="ref-card">
                            <div class="ref-front">
                                <span class="ref-category colleague">Colleague</span>
                                <h3 class="ref-name">Jennifer Kuehn, CPA, CFE</h3>
                                <p class="ref-title">Colleague, ATG/Cognizant</p>
                                <p class="ref-excerpt">Jace and I worked together for eight years, during which he consistently demonstrated deep expertise, reliability, and professionalism. Early in my tenure, Jace patiently trained me on complex billing software, ensuring I had the foundation needed to succeed. Over the years, we partnered on numerous initiatives that delivered significant impact for our customers.</p>
                                <div class="ref-front-actions">
                                    <span class="ref-flip-hint"><i class="fas fa-sync-alt"></i> Click to flip</span>
                                    <button class="ref-expand-btn" onclick="event.stopPropagation(); openModal(this);">Read Full</button>
                                </div>
                            </div>
                            <div class="ref-back">
                                <span class="ref-back-label">Contact Information</span>
                                <h3 class="ref-back-name">Jennifer Kuehn, CPA, CFE</h3>
                                <div class="ref-contact-row">
                                    <i class="fas fa-envelope"></i>
                                    <a href="mailto:Jenniferlelliott@yahoo.com">Jenniferlelliott@yahoo.com</a>
                                </div>
                                <div class="ref-contact-row">
                                    <i class="fas fa-phone"></i>
                                    <span>(406) 529-3716</span>
                                </div>
                                <div class="ref-relationship">
                                    <div class="ref-relationship-label">Relationship</div>
                                    <div class="ref-relationship-value">Colleague at ATG/Cognizant, 8 years</div>
                                </div>
                                <span class="ref-back-flip-hint"><i class="fas fa-sync-alt"></i> Click to flip back</span>
                            </div>
                        </div>
                        <div class="ref-full-text" style="display:none;">Jace and I worked together for eight years, during which he consistently demonstrated deep expertise, reliability, and professionalism. Early in my tenure, Jace patiently trained me on complex billing software, ensuring I had the foundation needed to succeed. Over the years, we partnered on numerous initiatives that delivered significant impact for our customers.<br><br>Jace has supported dozens of clients with exceptional results. One recent client was so impressed with his skill as a billing specialist\\u2014and the clarity and dependability of his work\\u2014that they requested he stay on and expand his role after completing an initial project. His communication is always professional, and his feedback on solutions and designs is grounded in best practices and thoughtful analysis. Jace is a trusted expert and a strong collaborator, and I recommend him without hesitation.<br><br><em>\\u2014 Jennifer Kuehn, CPA, CFE</em></div>
                    </div>
'''

# Insert before closing grid div
html = html.replace('                </div>\n            </div>\n        </section>', jennifer_card + '\n                </div>\n            </div>\n        </section>')

with open('references.html', 'w') as f:
    f.write(html)
print('Jennifer Kuehn reference added!')

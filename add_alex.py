with open('references.html', 'r') as f:
    html = f.read()

alex_card = '''
                    <!-- Alex Ekblad - Colleague -->
                    <div class="ref-card-wrapper" data-category="colleague">
                        <div class="ref-card">
                            <div class="ref-front">
                                <span class="ref-category colleague">Colleague</span>
                                <h3 class="ref-name">Alex Ekblad</h3>
                                <p class="ref-title">Colleague, ATG/Cognizant</p>
                                <p class="ref-excerpt">Jace is adaptive to difficult scenarios and consistently finds a way to move things forward. He is thorough and precise with his development work, and he is highly communicative to ensure teams are always on the same page.</p>
                                <div class="ref-front-actions">
                                    <span class="ref-flip-hint"><i class="fas fa-sync-alt"></i> Click to flip</span>
                                    <button class="ref-expand-btn" onclick="event.stopPropagation(); openModal(this);">Read Full</button>
                                </div>
                            </div>
                            <div class="ref-back">
                                <span class="ref-back-label">Contact Information</span>
                                <h3 class="ref-back-name">Alex Ekblad</h3>
                                <div class="ref-contact-row">
                                    <i class="fas fa-envelope"></i>
                                    <a href="mailto:alexekblad1@gmail.com">alexekblad1@gmail.com</a>
                                </div>
                                <div class="ref-contact-row">
                                    <i class="fas fa-phone"></i>
                                    <span>(715) 563-1393</span>
                                </div>
                                <div class="ref-relationship">
                                    <div class="ref-relationship-label">Relationship</div>
                                    <div class="ref-relationship-value">Colleague at ATG/Cognizant</div>
                                </div>
                                <span class="ref-back-flip-hint"><i class="fas fa-sync-alt"></i> Click to flip back</span>
                            </div>
                        </div>
                        <div class="ref-full-text" style="display:none;">Jace is adaptive to difficult scenarios and consistently finds a way to move things forward. He is thorough and precise with his development work, delivering high-quality results that the team can depend on. He is highly communicative, always making sure that everyone on the team is aligned and on the same page.<br><br><em>— Alex Ekblad, ATG/Cognizant</em></div>
                    </div>
'''

# Insert before closing grid div
html = html.replace('                </div>\n            </div>\n        </section>', alex_card + '\n                </div>\n            </div>\n        </section>')

with open('references.html', 'w') as f:
    f.write(html)
print('Alex Ekblad reference added!')

with open('references.html', 'r') as f:
    html = f.read()

new_card = '''
                    <!-- Ross Binkley - Partner -->
                    <div class="ref-card-wrapper" data-category="partner">
                        <div class="ref-card">
                            <div class="ref-front">
                                <span class="ref-category partner">Partner</span>
                                <h3 class="ref-name">Ross Binkley</h3>
                                <p class="ref-title">Chief Solutions Officer, GoTransverse</p>
                                <p class="ref-excerpt">I am pleased to recommend Jace Sullivan, whom I have had the opportunity to work with closely over several years. During that time, I have seen Jace grow into a highly capable and dependable professional with deep expertise in billing and monetization. Jace brings a strong combination of technical knowledge and problem-solving ability. His expertise while working with GT is at a level where he can confidently guide others, support new team members, and lead through complex implementations.</p>
                                <div class="ref-front-actions">
                                    <span class="ref-flip-hint"><i class="fas fa-sync-alt"></i> Click to flip</span>
                                    <button class="ref-expand-btn" onclick="event.stopPropagation(); openModal(this);">Read Full</button>
                                </div>
                            </div>
                            <div class="ref-back">
                                <span class="ref-back-label">Contact Information</span>
                                <h3 class="ref-back-name">Ross Binkley</h3>
                                <div class="ref-contact-row">
                                    <i class="fas fa-envelope"></i>
                                    <a href="mailto:rbinkley@gotransverse.com">rbinkley@gotransverse.com</a>
                                </div>
                                <div class="ref-contact-row">
                                    <i class="fas fa-phone"></i>
                                    <span>(512) 415-3189</span>
                                </div>
                                <div class="ref-relationship">
                                    <div class="ref-relationship-label">Relationship</div>
                                    <div class="ref-relationship-value">Partner — Chief Solutions Officer at GoTransverse</div>
                                </div>
                                <span class="ref-back-flip-hint"><i class="fas fa-sync-alt"></i> Click to flip back</span>
                            </div>
                        </div>
                        <div class="ref-full-text" style="display:none;">I am pleased to recommend Jace Sullivan, whom I have had the opportunity to work with closely over several years. During that time, I have seen Jace grow into a highly capable and dependable professional with deep expertise in billing and monetization.<br><br>Jace brings a strong combination of technical knowledge and problem-solving ability. His expertise while working with GT is at a level where he can confidently guide others, support new team members, and lead through complex implementations. He also has a strong foundation in mathematics and billing concepts, making him particularly effective in solving challenging pricing and usage-based scenarios.<br><br>One of Jace\'s most notable strengths is his work ethic. He consistently demonstrates ownership, reliability, and a commitment to delivering high-quality outcomes. He is someone I trust to take on difficult problems and see them through to completion. His broader experience as a solution architect in quote-to-cash processes and complex usage rating further reinforces his ability to operate effectively in demanding environments.<br><br>As Jace has progressed into a Solution Architect role, he has demonstrated strong leadership in guiding teams and delivering complex billing and monetization solutions. In his current capacity supporting a leading role at Cognizant, he drives architectural direction, mentors team members, and ensures successful execution across initiatives. He communicates solutions clearly and effectively, aligning technical approaches with business objectives. His experience leading engagements and navigating complex environments positions him well to continue expanding his impact at an enterprise level.<br><br>I strongly recommend Jace for roles that require analytical thinking, ownership, and expertise in billing and monetization.<br><br><em>— Ross Binkley, Chief Solutions Officer, GoTransverse</em></div>
                    </div>
'''

# Remove the sample cards and add the real one
# Find the grid opening and closing
old_samples = '''                    <!-- SAMPLE CARD 1 - Colleague -->
                    <div class="ref-card-wrapper" data-category="colleague">
                        <div class="ref-card">
                            <div class="ref-front">
                                <span class="ref-category colleague">Colleague</span>
                                <h3 class="ref-name">First Last</h3>
                                <p class="ref-title">Title, Company</p>
                                <p class="ref-excerpt">Paste the full reference text here. The card preview will truncate after five lines and the reader can expand to full screen to read the complete reference.</p>
                                <div class="ref-front-actions">
                                    <span class="ref-flip-hint"><i class="fas fa-sync-alt"></i> Click to flip</span>
                                    <button class="ref-expand-btn" onclick="event.stopPropagation(); openModal(this);">Read Full</button>
                                </div>
                            </div>
                            <div class="ref-back">
                                <span class="ref-back-label">Contact Information</span>
                                <h3 class="ref-back-name">First Last</h3>
                                <div class="ref-contact-row">
                                    <i class="fas fa-envelope"></i>
                                    <a href="mailto:email@example.com">email@example.com</a>
                                </div>
                                <div class="ref-contact-row">
                                    <i class="fas fa-phone"></i>
                                    <span>(000) 000-0000</span>
                                </div>
                                <div class="ref-relationship">
                                    <div class="ref-relationship-label">Relationship</div>
                                    <div class="ref-relationship-value">Colleague at ATG/Cognizant, 2018–2024</div>
                                </div>
                                <span class="ref-back-flip-hint"><i class="fas fa-sync-alt"></i> Click to flip back</span>
                            </div>
                        </div>
                        <div class="ref-full-text" style="display:none;">Paste the full reference text here. The card preview will truncate after five lines and the reader can expand to full screen to read the complete reference.</div>
                    </div>

                    <!-- SAMPLE CARD 2 - Partner -->
                    <div class="ref-card-wrapper" data-category="partner">
                        <div class="ref-card">
                            <div class="ref-front">
                                <span class="ref-category partner">Partner</span>
                                <h3 class="ref-name">First Last</h3>
                                <p class="ref-title">Title, Company</p>
                                <p class="ref-excerpt">Paste the full reference text here. This is a sample partner reference card that can be duplicated for each reference you want to add.</p>
                                <div class="ref-front-actions">
                                    <span class="ref-flip-hint"><i class="fas fa-sync-alt"></i> Click to flip</span>
                                    <button class="ref-expand-btn" onclick="event.stopPropagation(); openModal(this);">Read Full</button>
                                </div>
                            </div>
                            <div class="ref-back">
                                <span class="ref-back-label">Contact Information</span>
                                <h3 class="ref-back-name">First Last</h3>
                                <div class="ref-contact-row">
                                    <i class="fas fa-envelope"></i>
                                    <a href="mailto:email@example.com">email@example.com</a>
                                </div>
                                <div class="ref-contact-row">
                                    <i class="fas fa-phone"></i>
                                    <span>(000) 000-0000</span>
                                </div>
                                <div class="ref-relationship">
                                    <div class="ref-relationship-label">Relationship</div>
                                    <div class="ref-relationship-value">Implementation Partner, 2020–2023</div>
                                </div>
                                <span class="ref-back-flip-hint"><i class="fas fa-sync-alt"></i> Click to flip back</span>
                            </div>
                        </div>
                        <div class="ref-full-text" style="display:none;">Paste the full reference text here. This is a sample partner reference card that can be duplicated for each reference you want to add.</div>
                    </div>

                    <!-- SAMPLE CARD 3 - Client -->
                    <div class="ref-card-wrapper" data-category="client">
                        <div class="ref-card">
                            <div class="ref-front">
                                <span class="ref-category client">Client</span>
                                <h3 class="ref-name">First Last</h3>
                                <p class="ref-title">Title, Company</p>
                                <p class="ref-excerpt">Paste the full reference text here. This is a sample client reference card. Duplicate the entire ref-card-wrapper block for each new reference you want to add.</p>
                                <div class="ref-front-actions">
                                    <span class="ref-flip-hint"><i class="fas fa-sync-alt"></i> Click to flip</span>
                                    <button class="ref-expand-btn" onclick="event.stopPropagation(); openModal(this);">Read Full</button>
                                </div>
                            </div>
                            <div class="ref-back">
                                <span class="ref-back-label">Contact Information</span>
                                <h3 class="ref-back-name">First Last</h3>
                                <div class="ref-contact-row">
                                    <i class="fas fa-envelope"></i>
                                    <a href="mailto:email@example.com">email@example.com</a>
                                </div>
                                <div class="ref-contact-row">
                                    <i class="fas fa-phone"></i>
                                    <span>(000) 000-0000</span>
                                </div>
                                <div class="ref-relationship">
                                    <div class="ref-relationship-label">Relationship</div>
                                    <div class="ref-relationship-value">Client stakeholder, 2021–2023</div>
                                </div>
                                <span class="ref-back-flip-hint"><i class="fas fa-sync-alt"></i> Click to flip back</span>
                            </div>
                        </div>
                        <div class="ref-full-text" style="display:none;">Paste the full reference text here. This is a sample client reference card. Duplicate the entire ref-card-wrapper block for each new reference you want to add.</div>
                    </div>'''

html = html.replace(old_samples, new_card)

with open('references.html', 'w') as f:
    f.write(html)
print('Ross Binkley reference added, sample cards removed!')

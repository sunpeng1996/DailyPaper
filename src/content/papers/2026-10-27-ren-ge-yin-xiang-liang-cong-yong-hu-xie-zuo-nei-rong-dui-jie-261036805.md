---
title: 'Personality Latents: Conditioning Frozen Language Models on Individuals from
  Their Own Writing'
title_zh: 人格隐向量：从用户写作内容对冻结大模型做个性化适配
authors:
- Gunhee Cho
- Yun-Gyung Cheong
affiliations:
- Dept. of AI, Sungkyunkwan University
arxiv_id: '2610.36805'
url: https://arxiv.org/abs/2610.36805
pdf_url: https://arxiv.org/pdf/2610.36805
published: '2026-10-27'
collected: '2026-10-28'
category: LLM
direction: 大模型个性化 · 人格隐向量软前缀注入
tags:
- LLM Personalization
- Soft Prompt
- Personality Modeling
- Cross-LLM Transfer
- Prefix Tuning
one_liner: 无需人格标签与人工画像，从用户写作生成跨LLM可迁移人格隐向量，MBTI识别AUC达0.782
practical_value: '- 可借鉴「无标签用户隐向量优化+跨模型adapter适配」方案，落地电商Agent个性化：从用户历史评价、聊天记录生成用户偏好隐向量，无需人工打偏好标签，通过小adapter适配不同LLM底座，降低多基座部署成本

  - 可复用「训练时隐向量自由优化+推理时可选微调」的双模式设计：针对高价值用户，用少量历史交互数据对隐向量做几十步梯度微调，提升个性化效果，成本比全量fine-tune低数个量级

  - 可参考margin loss设计避免个性化退化：在用户偏好注入的训练中加入对比损失，确保当前用户的隐向量能比其他用户更好解释其行为，避免生成通用无差别的内容'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM人格/个性化控制方案存在三类局限：依赖人工撰写角色profile人力成本高，无法规模化落地；基于MBTI、大五人格等分类标签的方案粒度仅到群体级，无法适配个体差异；已有的用户嵌入方法受限于编码器表达上限，且绑定单一LLM底座，未验证是否能有效捕捉用户行为中隐含的个性化特征。

### 方法关键点
- 采用Generative Latent Optimization框架，每个训练用户的128维人格隐向量作为自由参数直接优化，不受编码器能力限制，仅以用户自身文本为监督信号，无需任何人格标签
- 训练轻量adapter将隐向量映射为24个软前缀token，拼接在prompt前注入冻结LLM，仅优化隐向量、adapter、编码器三类参数，LLM全量冻结
- 训练对称编码器预测隐向量实现新用户冷启动，推理阶段支持对新用户隐向量做60步梯度微调进一步提升效果
- 支持跨LLM复用同一用户隐向量，仅需为每个LLM训练独立的小adapter即可完成适配

### 关键结果
实验在Kaggle MBTI（8608人）、Essays（2081人大五标签）、PANDORA（1178人大五分数）三个数据集上开展，对比persona嵌入、prompt等基线：
- 面试场景提问下，优化后的人格隐向量MBTI识别AUC达0.782，领先最优基线0.127，跨三个不同的评分嵌入空间排名均保持第一
- 同一隐向量仅需适配新adapter即可迁移到Llama-3.1-8B，MBTI AUC达0.592，显著高于随机对照的0.492
- 推理侧60步隐向量微调可带来MBTI AUC 0.05-0.1的提升，仅需30秒/用户的计算成本

**最值得记住的结论**：用户个性化隐向量无需绑定单一LLM底座，通过轻量adapter即可跨模型迁移，推理侧少量梯度优化可大幅降低编码器能力限制带来的效果损耗

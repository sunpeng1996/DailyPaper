---
title: 'PACT: Defending Recommendation against Promotional News Rewriting via Attack-Diverse
  Score Consistency'
title_zh: PACT：基于多攻击源分数一致性的推荐系统推广改写攻击防御
authors:
- Chongxian Chen
- Fan Mo
- Xin Fan
- Hayato Yamana
affiliations:
- Waseda University
- ZOZO NEXT, Inc.
arxiv_id: '2611.00972'
url: https://arxiv.org/abs/2611.00972
pdf_url: https://arxiv.org/pdf/2611.00972
published: '2026-10-31'
collected: '2026-11-03'
category: RecSys
direction: 推荐系统鲁棒性 · 对抗文本攻击防御
tags:
- News Recommendation
- Adversarial Robustness
- Consistency Learning
- LLM Attack
- Text Rewriting
one_liner: 通过多源改写池采样对齐的无推理开销方案，防御LLM驱动的新闻推广改写攻击
practical_value: '- 电商/信息流文本感知推荐场景可直接复用PACT的池-采样-对齐框架：离线收集多LLM多策略生成的事实一致的商品/内容文案变体，训练时对齐同ID不同文案的排序打分，无需修改现有推荐架构、无推理额外开销，即可解决商家/内容方改文案刷排名的问题

  - 训练时固定每个样本每次采样的改写数量（如m=1），训练成本不随改写池规模增长，适配大规模业务的训练资源约束

  - 改写池构建优先加入针对业务排序目标优化的反馈类攻击变体，比仅加入风格类改写的防御效果提升更显著'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM驱动的推广改写攻击可在不改变事实的前提下，仅调整新闻/商品标题的措辞、风格就能操纵推荐排名，现有防御存在攻击覆盖不全、推理延迟高、训练成本随改写量线性增长的问题，无法适配大规模落地需求。
### 方法关键点
- **池化**：离线收集多生成器、多攻击策略（风格prompt、偏好微调、反馈优化）生成的事实一致改写，经实体校验、模型可见维度去重后为每个内容ID构建专属改写池
- **采样**：训练时每个样本每次出现都从池中随机采样固定数量（默认m=1）的改写，训练计算量不随池大小增长，为池级一致性目标提供无偏估计
- **对齐**：联合优化原样本的点击排序损失，以及同用户上下文下原样本与改写样本的打分一致性损失，正负样本分角色加权避免负样本主导训练
### 关键结果
在MIND-small数据集上测试3个主流新闻推荐 backbone（NAML/NRMS/LSTUR），对比无防御、Source Bias、SheepDog适配版3种基线：覆盖9种攻击+backbone组合，PACT推广率比最强基线最高低3.0个百分点，推理零额外延迟；推荐效用相对变化范围为-1.26%~+0.74%，几乎无损原有推荐效果；对未见过的生成器、未见过的攻击策略、自适应重训练的白盒攻击均保持鲁棒性。

文本感知型推荐系统可通过多源改写的分数一致性正则，在几乎不损失推荐效果、不增加推理开销的前提下，有效防御基于文本改写的排名操纵攻击。

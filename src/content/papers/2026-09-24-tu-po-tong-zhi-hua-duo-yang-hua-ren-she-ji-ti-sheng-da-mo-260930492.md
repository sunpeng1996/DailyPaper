---
title: 'Breaking Homogeneity: Diversifying Persona Sets for Creative LLM Outputs'
title_zh: 突破同质化：多样化人设集提升大模型输出创造性
authors:
- Sang Bin Moon
- Nicole Cho
- Daniel Borrajo
- Sumitra Ganesh
- Abolfazl Hashemi
affiliations:
- Purdue University
- J.P. Morgan AI Research
arxiv_id: '2609.30492'
url: https://arxiv.org/abs/2609.30492
pdf_url: https://arxiv.org/pdf/2609.30492
published: '2026-09-24'
collected: '2026-09-28'
category: LLM
direction: LLM人设多样化 · 生成创造力提升
tags:
- Persona Diversification
- TextGrad
- MCMC
- LLM Creativity
- Semantic Embedding
one_liner: 构建两轴人设多样化设计空间，提出4种方法大幅提升LLM输出多样性与创造性
practical_value: '- 电商多Agent生成营销文案、选品方案时，可复用进化式TextGrad人设生成方法，在保持98%+有效性的前提下提升输出多样性，避免方案同质化

  - 现有固定人设池的个性化推荐/智能客服场景，可直接套用COVERAGE/DISPERSION选择算法，零额外生成成本即可提升回复/内容的差异化程度

  - 人设优化与现有prompt工程、推理框架正交，现有业务的创造性prompt无需修改，搭配优化后的人设集即可进一步提升效果

  - 可直接复用基于embedding马氏距离的人设差异度量方法，比人工规则判断人设相似度更高效稳定'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
RLHF对齐后的LLM输出同质化严重，容易引发群体思维，在投资建议、创意生成等场景会带来系统性风险；现有基于人设的引导方法多为单点使用，缺乏集合层面的结构化优化，无法充分激发LLM隐含的发散性输出能力
### 方法关键点
- 构建两轴人设多样化设计空间：以「空间填充/边界探索」为多样性原则轴，「固定池选择/全新生成」为控制粒度轴，交叉覆盖4类优化路径
- 选择类算法：COVERAGE实现固定人设池内最大覆盖度最优选择，DISPERSION实现子集最小pairwise距离最大化的高分散选择，均有全局最优理论保证
- 生成类算法：UC-MCMC采样实现语义空间均匀覆盖生成，进化式TextGrad主动探索语义低密度边界，生成差异度更高的全新人设
### 关键实验
在AUT、Infinity-Chat、DAT三个创造性基准上测试，对比纯任务prompt、随机人设、创造力优化prompt、DMAD多智能体辩论等baseline：进化式生成人设比纯prompt提升78.8%响应多样性、26.1%原创性、49.5%灵活性、13.9%整体创造性，有效性保持98.5%；搭配创造力优化prompt可进一步提升18.6%多样性和6.3%创造性；Infinity-Chat上比随机人设的响应分离度提升近1倍
### 核心结论
人设集的几何结构而非单纯的人设存在本身，是驱动LLM输出多样性提升的核心，人设优化可与prompt工程、推理框架正交叠加复用

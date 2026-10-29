---
title: 'Same Verdict, Different Readers: Personalizing Fact-Checking Explanations
  from Relative Preferences'
title_zh: 基于相对偏好的高保真个性化事实核查解释改写方法
authors:
- Haokun Wen
- Xuemeng Song
- Mong-Li Lee
- Wynne Hsu
affiliations:
- National University of Singapore
- Southern University of Science and Technology
arxiv_id: '2610.37380'
url: https://arxiv.org/abs/2610.37380
pdf_url: https://arxiv.org/pdf/2610.37380
published: '2026-10-27'
collected: '2026-10-29'
category: LLM
direction: LLM偏好学习 · 个性化内容生成
tags:
- Personalization
- Preference Learning
- Natural Language Generation
- LLM Fine-tuning
- Fact Checking
one_liner: 提出PERPL框架，基于LLM模拟用户相对偏好实现高保真个性化事实核查解释改写
practical_value: '- 可复用「LLM模拟用户相对偏好+交叉配对生成监督信号」的范式，解决电商个性化文案生成场景下用户标注数据不足的问题，适配商品推荐理由、广告文案个性化改写等需求

  - 渐进式偏好优化的训练策略可直接迁移：先用轻量改写器在构造的监督数据上做基础训练，再用探索引导的偏好优化迭代，既降低训练成本又能突破预定义风格限制，适合个性化push文案、商品解释类内容生成场景

  - 区分用户个性化偏好与通用内容质量的思路可复用，在推荐理由、广告解释生成场景中避免为了个性化牺牲内容正确性/可读性，保证业务体感与事实准确性的平衡'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有事实核查系统的解释为统一生成，无法适配不同背景用户的阅读偏好，而用户手写参考解释的标注成本极高，同时需要兼顾个性化适配与事实保真的平衡，突破预定义解释风格的限制。
### 方法关键点
PERPL为两阶段框架：1）模拟偏好构造模块，通过跨角色交叉配对策略，从LLM模拟的读者相对偏好中提取角色专属监督信号，区分个性化偏好与通用内容质量；2）渐进式偏好学习模块，先用构造的监督数据训练轻量改写器，再通过探索引导的偏好优化迭代，可生成预定义风格外的用户偏好内容。
### 关键结果
实验验证PERPL在个性化偏好对齐指标上显著优于参数量远大于自身的通用LLM，同时保持极高的事实保真度，无需依赖用户手写的参考解释作为训练监督。

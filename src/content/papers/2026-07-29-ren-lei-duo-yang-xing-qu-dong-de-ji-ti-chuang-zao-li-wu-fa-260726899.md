---
title: Human diversity fuels collective creativity that large language models cannot
  simulate or sustain
title_zh: 人类多样性驱动的集体创造力无法被大语言模型模拟或维持
authors:
- Mengchen Dong
- Hiromu Yakura
affiliations:
- Max Planck Institute for Human Development
- Center for Humans and Machines
arxiv_id: '2607.26899'
url: https://arxiv.org/abs/2607.26899
pdf_url: https://arxiv.org/pdf/2607.26899
published: '2026-07-29'
collected: '2026-08-02'
category: LLM
direction: 大语言模型创意生成能力边界研究
tags:
- LLM
- Creativity
- Human-AI Collaboration
- Diversity
- Generative AI
one_liner: 通过多组对照实验证实人类集体创意多样性无法被现有LLM模拟，AI精修比AI生成更能保留多样性
practical_value: '- 电商营销文案、商品卖点批量生成场景优先采用「人类初版创意+AI精修」的 workflow，避免全AI生成导致的创意同质化，降低用户审美疲劳带来的长期转化率下跌

  - 用LLM模拟不同用户群体做推荐系统离线评估、创意A/B测试时，不可完全依赖模拟结果，LLM生成的用户反馈多样性远低于真实人群，易导致评估偏差

  - 跨境电商内容生产场景可允许非母语创作者用母语构思再由AI转译润色，既能提升个体内容质量，也能保留集体创意多样性，适配不同区域用户偏好'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
生成式AI普及下存在两个待验证风险：AI辅助会同质化不同人群的创意产出，AI模拟的多样性可替代真实人类创意，直接影响内容生产、创意评估等业务的长期效果。
### 方法关键点
开展预注册创意隐喻对照实验，对象覆盖母语（L1）/非母语（L2）英语写作者，分三组对照：无AI创作、AI直接生成创意、AI精修人类初版创意；后续用参与者真实背景构建persona，测试3类LLM、原生语言prompt、调高采样温度下的模拟创意池多样性。
### 关键结果
- L2写作者集体创意多样性显著高于L1群体，母语构思场景下创意池多样性最高
- AI生成创意会压缩所有群体的集体多样性，L2群体的多样性优势完全消失；AI精修可完整保留两类群体的多样性
- 所有LLM模拟的创意池多样性均低于全部人类创意池，调高采样温度仅能通过生成无意义文本提升假多样性

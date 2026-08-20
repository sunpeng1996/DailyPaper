---
title: 'TractorBeam: Personalized AI Sensemaking Support via Collaborative Machine
  Annotation'
title_zh: TractorBeam：基于协作机器标注的个性化AI语义理解支持系统
authors:
- Sireesh Gururaja
- Jordan Taylor
- Emma Strubell
affiliations:
- Carnegie Mellon University
- Language Technologies Institute
arxiv_id: '2608.18994'
url: https://arxiv.org/abs/2608.18994
pdf_url: https://arxiv.org/pdf/2608.18994
published: '2026-08-19'
collected: '2026-08-20'
category: LLM
direction: LLM 人机协作文档语义理解
tags:
- Human-AI Collaboration
- Document Sensemaking
- In-context Annotation
- LLM Application
- Factuality Assurance
one_liner: 提出浏览器插件形态的协作机器标注系统，将LM输出转为上下文高亮，解决语义理解工具事实性与溯源问题
practical_value: '- 可复用「LLM输出转上下文内可验证标注建议」的交互设计，解决电商商品详情、用户评价的LLM摘要事实性错误问题

  - 人机迭代标注的反馈回路可迁移到推荐系统用户偏好冷启动场景，通过少量显式标注快速对齐用户个性化需求

  - 浏览器插件形态的轻量交互方案可快速搭建面向电商运营的个性化文档（竞品分析、用户评论）分析工具'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有基于LLM的文档问答类语义理解工具存在两大核心痛点：一是输出事实性差、缺乏可追溯的来源依据，二是天然引导用户做验证性查询而非探索性研究，难以匹配用户个性化的认知框架需求。
### 方法关键点
1. 构建浏览器插件形态的混合主动式系统TractorBeam，提出「协作机器标注」交互范式，将LM输出直接转换为PDF上下文内的高亮建议，从交互层面天然解决溯源问题
2. 支持用户自定义标注规则、通过显式正负例标注反馈迭代对齐LM输出与用户的个性化认知框架
### 关键结果
初步用户研究显示100%参与者认为系统可帮助评估、迭代优化LM对自身标注意图的拟合度，多名参与者表示LM给出的高亮建议使其重新调整了原有的认知框架

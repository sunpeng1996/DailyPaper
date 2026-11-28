---
title: A Survey of Security, Privacy, and Ethics of Large Language Models in Telecom
title_zh: 电信领域大语言模型的安全、隐私与伦理研究综述
authors:
- Joy Bose
- Srinivas Adyapak
affiliations:
- Ericsson
arxiv_id: '2611.34868'
url: https://arxiv.org/abs/2611.34868
pdf_url: https://arxiv.org/pdf/2611.34868
published: '2026-11-25'
collected: '2026-11-28'
category: LLM
direction: 电信领域LLM安全隐私伦理研究
tags:
- LLM
- Security
- Privacy
- Ethics
- Telecom
one_liner: 梳理电信场景LLM部署的安全隐私伦理风险，构建领域专属分类框架并明确开放研究挑战
practical_value: '- 处理电商/推荐场景高敏感用户数据（收货信息、浏览轨迹、支付记录）时，可参考文中敏感数据分类思路，梳理LLM调用全链路的泄露风险点

  - 跨境电商/出海推荐业务的LLM部署可参考跨域合规挑战分析，提前规避数据跨境传输、用户隐私合规相关风险

  - 基于用户长周期时序行为的LLM推荐/Agent应用，可参考纵向数据隐私风险防范思路，降低用户重识别、数据泄露概率'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
电信行业已广泛将LLM应用于客服、网络分析、运营支撑等场景，但电信数据具备高敏感、长时序、多维度关联的特性，叠加LLM的黑盒属性，导致部署面临独特的安全、隐私与伦理风险，缺乏场景化的风险梳理与防护体系参考。
### 方法关键点
1. 对比电信数据与医疗、金融等领域敏感数据的差异，明确电信数据特有的高重识别风险、匿名化效果随时间易失效等核心问题
2. 构建电信专属的安全隐私伦理分类框架，将三类风险与具体业务场景一一映射
3. 梳理现有防护手段的不足，提炼领域未解决的核心研究挑战
### 关键发现
明确三大核心开放研究方向：长时序数据隐私保护技术、跨边境合规适配机制、可扩展的LLM护栏方案

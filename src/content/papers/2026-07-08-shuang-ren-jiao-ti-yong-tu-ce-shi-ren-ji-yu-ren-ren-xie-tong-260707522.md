---
title: 'Two-player Alternate Uses Test: A Controlled Testbed for Interactive Human-AI
  and Human-Human Co-Creation'
title_zh: 双人交替用途测试：人机与人人协同创作可控测试平台
authors:
- Babak Hemmatian
- Anita Keshmirian
- Yijun Lin
- Shravan Ramamoorthy
- Maryam Jahadakbar
- Eli Khuri-Reid
- Jingtong Wang
- Sarah Hadjarab
- Sindre Veum
- Pranav Gupta
affiliations:
- Stony Brook University
- Forward College Berlin
- Alinea
- University of Illinois Urbana-Champaign
- University of California San Diego
arxiv_id: '2607.07522'
url: https://arxiv.org/abs/2607.07522
pdf_url: https://arxiv.org/pdf/2607.07522
published: '2026-07-08'
collected: '2026-07-10'
category: Agent
direction: 人机协同创作 · 可控测试床
tags:
- Human-AI Collaboration
- Co-Creation
- Testbed
- Creativity
- GPT-4
- Alternate Uses Test
one_liner: 提出双人扩展版AUT测试床，支持匹配条件下人机、人人协同创作的效果对比与归因
practical_value: '- 可复用双人交替创作的实验框架，用于评估运营+LLM协同生成电商文案、商品卖点的效果，控制变量排除混杂因素

  - 可借鉴「创意种子」干预方法，给文案生成Agent提前投喂高创意历史样本，直接提升产出内容的原创性

  - 可复用该测试床的因素拆分逻辑，拆解影响人机协同推荐文案效果的用户特征、Agent感知、内容动态三类因子，针对性优化'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有AI创意研究要么对比独立Agent无法反映协同过程，要么实地研究缺少实验控制，难以准确归因人机/人人协同创作的效果差异。
### 方法关键点
扩展经典Alternate Uses Test（AUT）为双人交互版本，在匹配时间、交互规则的条件下对比人人、人机协同表现，可将性能拆分为参与者特质、合作伙伴感知、内容动态三个原本混杂的因子，配套开源平台、代码和数据集。
### 关键结果
62人线下试点显示，相同时间限制下，与GPT-4搭档的创意原创性和与人类搭档无统计显著差异；高趋近动机（BAS Drive）的参与者从协同中获得的原创性提升更明显；提前接触高创意样本可提升后续表现，验证了「创意种子」干预的有效性。

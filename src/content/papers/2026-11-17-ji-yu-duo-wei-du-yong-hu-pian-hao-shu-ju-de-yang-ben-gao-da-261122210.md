---
title: Sample-efficient Personalization of Large Language Model Alignment with Multidimensional
  User Preference Data
title_zh: 基于多维度用户偏好数据的样本高效大语言模型个性化对齐
authors:
- Zhen-Yu Zhang
- Jerry Huang
- Gang Niu
- Takashi Ishida
- Masashi Sugiyama
affiliations:
- RIKEN
- Université de Montréal
- Mila - Quebec AI Institute
- The University of Tokyo
arxiv_id: '2611.22210'
url: https://arxiv.org/abs/2611.22210
pdf_url: https://arxiv.org/pdf/2611.22210
published: '2026-11-17'
collected: '2026-11-18'
category: Training
direction: LLM偏好对齐 · 样本效率优化
tags:
- DPO
- Preference Alignment
- Sample Efficiency
- Personalization
- Pareto Cone
- Online Learning
one_liner: 提出MPG-DPO方法，基于个性化偏好锥引导响应对选择，提升LLM偏好对齐样本效率
practical_value: '- 做电商个性化文案生成、智能客服Agent、生成式推荐对齐时，可复用多维度偏好锥思路，用低成本自动评分器（如相关性、吸引力、合规性等业务自定义维度）预过滤劣质候选，降低昂贵的人工/大模型标注成本

  - 在线DPO训练阶段可借鉴max-min响应对选择策略，优先选择当前偏好规则存在冲突的候选对做标注，同等标注预算下对齐效果提升显著

  - 工程实现可直接复用pycddlib库完成偏好锥的双描述法计算，结合LoRA做轻量对齐训练，无需改动原有DPO训练管线，落地成本低

  - 针对用户差异化的偏好权衡需求（如部分用户偏好简洁、部分偏好信息全面），可动态更新不同用户的偏好锥，无需重新训练全局模型即可实现快速个性化适配'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
在线LLM偏好对齐的标注成本极高、样本效率低下，现有方法仅从模型视角选择高不确定性响应对，往往浪费预算标注用户历史偏好已能明确排序的无效对；同时通用对齐规则无法适配用户个性化的多维度偏好权衡（如电商用户愿意牺牲部分文案简洁性换取更高商品信息完整性），亟需低成本的个性化对齐方案。

### 方法关键点
- 为每个响应对做多维度自动打分（如正确性、完整性、清晰度等维度，成本远低于人工偏好标注），基于历史用户比较结果构建个性化偏好锥，明确用户的偏好权衡方向
- 每轮在线DPO训练时，先用偏好锥过滤明显被支配的劣质响应，再从剩余候选中选择偏好冲突最显著的响应对，最大化单次标注的信息增益
- 得到标注后同步更新偏好锥和LLM策略，理论证明随训练推进，无效标注的占比会趋近于0

### 关键实验
在Qwen2.5-7B、Mistral-7B、OLMo-2-7B三个7B模型上验证，和Online DPO、XPO、APL等SOTA基线比，相同标注预算下，MPG-DPO在ALPACAEVAL2上最高提升1.68pct，ARENA-HARD最高提升1.36pct，TL;DR摘要胜率最高提升1.93pct；消融实验证明偏好锥过滤、冲突对选择、动态锥更新三个模块均有明确收益。

### 核心结论
利用低成本多维度自动评分构建用户偏好锥，把标注资源集中到真正存在偏好权衡的响应对上，是提升LLM对齐样本效率的核心可行路径。

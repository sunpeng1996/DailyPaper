---
title: 'The Dual-Tier Sentiment Framework: Scalable Multimodal UX Attribution in Web
  Search'
title_zh: 双层情感框架：网页搜索场景下可扩展的多模态UX归因方案
authors:
- Yi Ding
- Gaurav Kumar
- Rui Min
- Isabella Ye
- Bhavika Goyal
- Emilio Antunez
- Huihui Chen
- Ke Xu
- Xiaowei Sun
- Xin Xu
affiliations:
- Google
arxiv_id: '2611.27899'
url: https://arxiv.org/abs/2611.27899
pdf_url: https://arxiv.org/pdf/2611.27899
published: '2026-11-20'
collected: '2026-11-23'
category: Eval
direction: 多模态UX评估 · LLM自动化归因
tags:
- UX_Attribution
- Multimodal_LLM
- A-B_Testing
- RL_Prompt_Optimization
- AI_Judge
one_liner: 提出并行双层多模态UX归因框架，大幅压缩搜索A/B实验的用户体验评估耗时并提升诊断精度
practical_value: '- 可复用双层评估架构：上层用轻量微调小模型做高吞吐粗筛拦截明显负向实验，下层用MLLM做精准根因诊断，平衡成本与精度，适配电商推荐/搜索大规模A/B实验评估场景

  - 可迁移User Toil量化方法：基于结果块空间坐标、点击后落地页质量综合计算用户浏览/操作成本，可直接用于电商搜索结果页、商品详情页的UX效果量化

  - RL驱动的自动化Prompt优化方案可复用：用轻量Mentor模型生成Prompt喂给冻结的大模型Student，结合AI Judge做奖励信号，避免人工Prompt调优的过拟合问题，降低大模型评估的维护成本

  - 做用户主观体验评估时，需用多轮AI Judge+人工校验过滤与UI无关的用户偏误（比如对广告的天然反感），避免评估指标被噪声干扰'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
大规模Web搜索/广告平台的高频A/B实验依赖用户体验(UX)评估，传统人工问卷评估延迟高（周级）、成本高，而基于点击、滚动深度等自动化指标无法定位视觉空间类的UX异常（比如广告标识不明显、布局混乱导致的用户摩擦），也无法做根因诊断，亟需兼顾规模化和细粒度的UX归因方案。

### 方法关键点
- 采用并行双层架构，同时满足高吞吐粗筛和细粒度诊断需求：Tier1（宏观系统）基于Gemini XS微调的双编码器-解码器LLM，输入词法特征、元数据、用户交互信号，输出整体页面的用户情感回归结果，解码器生成的CoT仅作为训练时的正则项，不增加推理开销
- Tier2（微观系统）基于Gemini 3.0 Pro MLLM，输入SRP渲染图、bounding box坐标、用户query意图、落地页摘要，量化User Toil（用户找到满意结果的总认知+时间成本），作为UX好坏的核心指标
- 配套RL驱动的Mentor-Student自动Prompt优化框架，以及AI Judge做SxS评估对齐人类标注，无需全量微调MLLM即可提升评估准确率

### 关键实验
- Tier1在50万+条holdout数据上，PR-AUC比仅用词法特征的基线高9.8%，实验级检测precision提升20%，评估延迟从周级降到小时级，减少40%以上的问卷成本
- Tier2在千级专家标注+真实用户调研数据上，先通过注入bounding box特征获得5%的F1提升，再叠加RL自动Prompt优化再获得1.5%+的F1提升，整体F1超基线6.5%

### 核心结论
大规模产品实验的用户体验评估必须走「粗筛+精诊」的分层架构，才能同时满足规模化、低成本、可诊断三个核心需求，纯人工或纯粗粒度指标都无法适配高速迭代的互联网产品迭代节奏。

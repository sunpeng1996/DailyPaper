---
title: 'Beyond Trial-and-Error: Agentic Optimization for Image-to-Video Adherence'
title_zh: 超越试错：面向图像转视频内容一致性的智能体优化框架
authors:
- Aman Tyagi
- Hemanth Boinpally
- Jonathan Chen
- Douglas Gebert
- Steven Hickson
affiliations:
- Google Cloud
- Google DeepMind
arxiv_id: '2608.12290'
url: https://arxiv.org/abs/2608.12290
pdf_url: https://arxiv.org/pdf/2608.12290
published: '2026-08-12'
collected: '2026-08-13'
category: Agent
direction: Agent 生成式内容对齐优化
tags:
- Agentic Optimization
- Image-to-Video
- Prompt Tuning
- Bayesian Optimization
- Multimodal LLM
- Generative Content
one_liner: 两阶段智能体框架自动优化I2V的prompt与超参数，人类偏好win率最高达69%
practical_value: '- 电商/广告短视频生成场景可直接复用两阶段优化范式：先通过结构化评估迭代优化prompt，再用贝叶斯搜索调优CFG、种子等超参，相比人工试错可降低50%以上的生成成本

  - 生成内容的一致性校验可复用DSG+CMQ结构化问答方法，相比CLIP相似度打分，对语义一致性、生成瑕疵的识别准确率更高，可大幅减少人工审核量

  - 贝叶斯优化混合离散（随机种子）、连续（CFG scale）参数空间的实现方案，可迁移到所有AIGC类任务的超参调优流程，比随机/网格搜索效率提升3-5倍

  - 自研生成内容质量指标时可参考VTA的层级加权设计，根节点错误直接清零子节点得分，更贴合人类对内容优先级的判断逻辑'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前黑盒Image-to-Video（I2V）模型随机性极强，prompt、超参数的微小变动就会导致输出结果差异巨大，电商广告、专业内容生产等场景要求生成内容严格对齐创意brief，现有依赖人工试错的生产流程效率极低、算力成本极高，亟需系统化的优化框架解决可控性问题。

### 方法关键点
- 提出两阶段Agentic Self-Improvement闭环优化框架，分步骤解决prompt语义对齐、超参数随机波动两大核心误差来源。
- Prompt优化阶段：用mLLM自动生成两套结构化评估问题，Davidsonian Scene Graph（DSG）校验语义元素一致性，Common Mistake Questions（CMQ）检测生成瑕疵/时序一致性问题，迭代重写prompt直到Video-Text Adherence（VTA）得分最高；其中Gemini 2.5 Pro作为VQA评估器的准确率可达DSG 92%、CMQ 82%，与人工判断高度一致。
- 超参数优化阶段：采用贝叶斯优化同时搜索连续的CFG scale（取值1-15）和离散的随机种子，基于VTA+RAHF（人类偏好模拟）+UVQ（视频质量）多目标奖励引导搜索，相比随机搜索大幅减少无效试错。

### 关键结果
基于V-Bench数据集的100组图像-prompt对，用Veo 2.0作为基底I2V模型开展人类偏好评估：100轮搜索下，框架生成视频的人类偏好win率最高达69%（vs 随机搜索基线），对比更强的Best-of-Random（100次随机生成后选最优）基线，win率仍达42%（vs 基线的8%）。

**最值得记住的结论**：将生成式内容生产从开环试错模式重构为闭环目标导向的优化，是AIGC落地工业级生产场景的核心路径。

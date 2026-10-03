---
title: 'EgoTools: Towards Tool-Centric Reasoning in Real-World Egocentric Videos'
title_zh: EgoTools：面向真实世界第一人称视频的工具中心推理资源套件
authors:
- Shulin Tian
- Junsu Kim
- Shuai Liu
- Hao Li
- Yujiao Shen
- Sihan Li
- Zhe Yang
- Yeongon Kim
- Feiyu Li
- Jialin Wu
affiliations:
- S-Lab, Nanyang Technological University
- A*STAR
- KAIST
- PKU
- University of Catania
arxiv_id: '2609.39378'
url: https://arxiv.org/abs/2609.39378
pdf_url: https://arxiv.org/pdf/2609.39378
published: '2026-09-29'
collected: '2026-10-03'
category: Agent
direction: 具身Agent · 工具使用推理
tags:
- Embodied Agent
- Egocentric Video
- Tool Use Reasoning
- Multimodal LLM
- Benchmark
- Dataset
one_liner: 推出包含100小时第一人称工具数据集和千题评测基准的EgoTools套件，支撑具身Agent工具推理训练评估
practical_value: '- 电商AR导购/具身选品Agent团队可复用EgoTools的工具affordance标注逻辑，优化商品使用场景推理能力

  - 工业级多模态Agent评测可借鉴EgoTools-Bench的分层任务设计，从感知、几何、流程到因果分维度拆解能力短板

  - 多模态大模型微调数据构造可参考EgoTools-Data的「视频+音频+标注+3D信息」同步范式，提升微调数据质量'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前多模态视频模型的工具中心具身推理能力短板明显，缺乏真实世界第一人称工具使用数据与针对性评测基准，限制了具身Agent的落地能力。
### 方法关键点
推出EgoTools统一资源套件，包含两大互补组件：
1. EgoTools-Data：100小时工具中心第一人称视频语料，同步标注音频、密集字幕、重推理旁白及补充3D信息
2. EgoTools-Bench：覆盖感知与接地、几何、流程、因果推理4个赛道的1000道QA对诊断基准
### 关键结果
- Gemini-3.1-Pro 整体准确率仅66.9%，感知与接地赛道准确率仅51.7%
- 用EgoTools-Data做全监督微调（严格分离训练测试视频），Qwen3-VL-8B-Instruct 基准准确率从50.0%提升至60.9%

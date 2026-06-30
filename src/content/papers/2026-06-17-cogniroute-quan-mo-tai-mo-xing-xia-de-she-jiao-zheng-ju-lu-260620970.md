---
title: 'CogniRoute: Learning to Route Social Evidence in Omni-Modal Models'
title_zh: CogniRoute：全模态模型下的社交证据路由学习方法
authors:
- Yifan Shen
- Pei Tian
- Xinzhuo Li
- Bowen Fang
- Shujun Xia
- Bingxuan Li
- Ana Jojic
- Wenming Ye
- Xu Cao
- James Matthew Rehg
affiliations:
- University of Illinois Urbana-Champaign
- Columbia University
- Google
arxiv_id: '2606.20970'
url: https://arxiv.org/abs/2606.20970
pdf_url: https://arxiv.org/pdf/2606.20970
published: '2026-06-17'
collected: '2026-06-30'
category: Multimodal
direction: 多模态推理 · MoE路由优化
tags:
- MoE
- Multimodal Reasoning
- Video QA
- Routing Mechanism
- Benchmark
one_liner: 提出schema引导的MoE全模态社交推理框架与118K标注社交视频QA数据集，精度显著优于现有基线
practical_value: '- 电商直播QA、短视频内容理解场景可复用该schema引导的MoE路由逻辑，按模态关系、推理需求分配专家，降低无效模态信息干扰

  - 多模态任务训练时可引入路由感知RL优化，叠加正确性、模态一致性、证据时序匹配多维度奖励，同时对齐生成结果与专家分配

  - 构建多模态业务评测集可参考OmniSocialBench的标注范式，新增推理轨迹、证据跨度、schema标签维度，便于定位bad case根因'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有全模态模型虽可同时处理音视频、文本，但无法针对任务需求精准调用对应模态证据，在依赖跨模态关联、时序线索、冲突消解的社交视频QA场景下效果缺陷明显。
### 方法关键点
- 提出schema引导的MoE全模态推理框架CogniRoute，训练阶段引入认知schema按跨模态关系、推理需求、时序范围拆分样本，监督微调阶段对齐全局路由签名与该结构
- 新增路由感知强化学习，结合答案正确性、模态一致性推理、认知时序grounding三类奖励，联合优化token生成与专家分配
- 构建包含118K结构化样本的OmniSocialBench社交视频QA数据集，标注推理轨迹、schema标签、时序证据跨度
### 关键结果
在OmniSocialBench上平均准确率达59.38%，较最强专有基线提升15.33pp，较最强开源全模态基线提升26.77pp，在需音视频协同、冲突消解、时序社交推理的任务上增益最大

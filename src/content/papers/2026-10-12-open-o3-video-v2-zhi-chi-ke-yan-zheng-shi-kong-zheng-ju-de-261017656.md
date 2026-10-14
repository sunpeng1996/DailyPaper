---
title: 'Open-o3-Video-v2: Seek, Ground, and Reason with Verifiable Spatio-Temporal
  Evidence'
title_zh: Open-o3-Video-v2：支持可验证时空证据的主动视频推理框架
authors:
- Jiahao Meng
- Zhongyuan Bao
- Yue Tan
- Haiquan Wen
- Renrui Zhang
- Anna Wang
- Jason Li
- Yanwei Fu
- Yunhai Tong
- Ming-Hsuan Yang
affiliations:
- PKU
- FDU
- NTU
- UC Merced
arxiv_id: '2610.17656'
url: https://arxiv.org/abs/2610.17656
pdf_url: https://arxiv.org/pdf/2610.17656
published: '2026-10-12'
collected: '2026-10-14'
category: Agent
direction: 多模态Agent · 视频时空证据推理
tags:
- Multimodal Agent
- Video Reasoning
- GRPO
- Spatio-Temporal Grounding
- RLHF
one_liner: 提出整合证据主动搜索、时空对齐、推理的多模态Agent框架，在多视频基准上显著优于基线
practical_value: '- 电商短视频/直播内容理解场景可复用seek-ground-reason流程，主动裁剪关键片段做细粒度商品/动作识别，无需全量帧处理降低算力开销

  - Agent工具调用奖励可借鉴CS-GRPO设计，追踪每轮调用的信息增益，惩罚重复/无效调用，适配电商导购Agent、多轮搜索query理解等场景

  - 多轮推理SFT数据构造方法可迁移：先过滤无需工具调用的简单样本，再标注关键证据、重写CoT轨迹，大幅降低人工标注成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视频推理MLLM要么依赖初始固定采样帧容易漏关键线索，要么Agent式片段检索没有和推理过程的时空证据对齐，结果不可追溯，长视频细粒度推理准确率低，同时缺乏适配多轮证据获取的监督数据和奖励机制。

### 方法关键点
- 采用seek-ground-reason的Agent推理范式，模型可主动调用`crop_video`工具获取目标时段不同采样密度的片段，将时间戳、物体bounding box直接嵌入推理链作为可验证证据
- 构造STGR-v2-CoT-135K数据集，包含52K多轮工具调用推理轨迹，配套STGR-v2-RL-13K用于RL优化
- 提出Clue-Seek GRPO（CS-GRPO）奖励机制，追踪每轮工具调用后的证据覆盖度变化，奖励有效信息增益，惩罚无效、重复、碎片化的工具调用

### 关键结果
在V-STaR时空推理基准上，4B版本较Qwen3-VL-4B基线mAM提升8.5%、mLGM提升12.6%；在长视频推理基准Video-Holmes、LVBench上分别提升10.7%、7.2%；8B版本V-STaR mLGM达56.5%，Charades-TimeLens时序定位mIoU达51.1%。

### 核心结论
主动证据获取和可验证的物体级时空对齐是可靠长序列细粒度推理的两个互补核心能力。

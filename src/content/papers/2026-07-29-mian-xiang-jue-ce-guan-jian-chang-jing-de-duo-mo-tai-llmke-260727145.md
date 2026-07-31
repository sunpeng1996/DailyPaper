---
title: Explainable and Resource-Efficient Spatial Reasoning in Multimodal LLMs for
  Decision-Critical Applications
title_zh: 面向决策关键场景的多模态LLM可解释高效空间推理方法
authors:
- Piyush Jain
- Kousik Dasgupta
- Rajarshi Roy
- Subarna Tripathi
affiliations:
- Heritage Institute of Technology, Kolkata
- Kalyani Government Engineering College
- IAIRO
- Intel Corporation
arxiv_id: '2607.27145'
url: https://arxiv.org/abs/2607.27145
pdf_url: https://arxiv.org/pdf/2607.27145
published: '2026-07-29'
collected: '2026-07-31'
category: Reasoning
direction: 多模态大模型 · 免训练空间推理优化
tags:
- MLLM
- Spatial Reasoning
- Training-free
- Hallucination Reduction
- Prompt Engineering
- Resource Efficient
one_liner: 免训练ByDeWay-V2框架融合深度分层与显式空间谓词，提升MLLM空间推理能力与可解释性
practical_value: '- 电商多模态内容审核可直接复用该框架：比如检测直播场景中主播与商品的空间关系、违规物品摆放位置，无需微调MLLM，仅通过注入YOLO提取的空间谓词即可提升判断准确率，输出的显式谓词还可作为合规审计依据

  - 端侧导购/巡检Agent的空间感知优化：可采用仅保留空间谓词的轻量化配置，在<40token的上下文预算下提升端侧轻量MLLM的空间判断能力，适配硬件资源有限的线下货架巡检、家庭导购机器人等场景

  - 多模态生成式推荐幻觉缓解：基于用户上传的家居/穿搭场景图生成商品推荐时，可先提取场景中已有物品的空间关系作为prompt约束，避免MLLM推荐不符合空间逻辑的商品（如在餐桌区域推荐衣柜），降低幻觉'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
MLLM在机器人、具身AI、安全监控等决策关键场景落地时，存在两大核心痛点：一是空间推理能力不足，对同一深度平面内物体的投射、拓扑等细粒度空间关系判断准确率低；二是黑箱特性缺乏可解释性，判断结果无法审计，同时已有免训练的深度分层提示（LDP）方法无法解决同层物体的空间关系判断问题，幻觉问题突出，亟需可解释、资源高效的免训练方案补足能力短板。

### 方法关键点
- 双分支免训练架构：上分支采用YOLO-World-L开放词汇检测器提取物体边界框，通过计算IoU、中心点距离、重叠率等几何特征，生成「物体A在物体B左侧/内部/附近」等人类可读的显式空间谓词；下分支用DepthAnything V2生成深度图，分近中远三层后用KOSMOS-2生成各层描述，得到深度分层提示。
- 混合提示构建：将深度分层描述、显式空间谓词和用户Query拼接后输入MLLM，无需微调任何模型参数，同时支持低资源场景下仅保留空间谓词的轻量化配置，适配40token以内的上下文限制。

### 关键结果
在VSR、POPE、BLINK三个基准上测试Qwen2.5-VL、BLIP-Base、ViLT三个模型，对比基线LDP方法：BLINK空间子集上Qwen2.5-VL的F1相对提升46%，从0.496提升到0.727；VSR基准上BLIP-Base的F1从接近随机的0.053提升到0.525，实现近10倍性能提升；POPE幻觉测试集上BLIP-Base的准确率从86%提升到90.67%，F1从0.873提升到0.919；轻量化配置可在CPU上运行，上下文预算低于40token。

### 核心结论
免训练的显式几何空间谓词注入，是低成本提升MLLM空间推理准确率、可解释性和资源效率的有效路径，尤其适配参数规模小、缺乏空间专项训练的轻量MLLM。

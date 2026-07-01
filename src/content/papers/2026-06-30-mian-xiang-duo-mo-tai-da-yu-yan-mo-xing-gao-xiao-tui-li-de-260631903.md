---
title: 'Attend, Transform, or Silence: Operator-Level Visual Skipping for Efficient
  Multimodal LLM Inference'
title_zh: 面向多模态大语言模型高效推理的运算符级视觉跳过方法
authors:
- Zhaoyang Luo
- Runmin Dong
- Miao Yang
- Fan Wei
- Yushan Lai
- Bin Luo
- Haohuan Fu
affiliations:
- 清华大学深圳国际研究生院
- 中山大学
- 国家超级计算深圳中心
- 清华大学
arxiv_id: '2606.31903'
url: https://arxiv.org/abs/2606.31903
pdf_url: https://arxiv.org/pdf/2606.31903
published: '2026-06-30'
collected: '2026-07-01'
category: LLM
direction: 多模态大模型 · 推理效率优化
tags:
- MLLM
- Inference Acceleration
- Transformer
- Visual Token
- Operator Skipping
one_liner: 通过算子粒度的视觉冗余跳过，在保留99.5%性能的前提下降低33.7%的MLLM推理计算量
practical_value: '- 部署电商多模态导购/商品理解MLLM时，可复用算子级跳过思路，无需改动模型权重，仅通过少量无标注样本校准确定每层冗余算子，即可实现推理提速，避免token
  pruning带来的OCR、细粒度商品属性识别损失

  - 复用answer-observable的冗余判断指标，不需要标注数据即可定位推理中对最终输出无影响的冗余计算，适配业务场景的个性化冗余分布

  - 该策略可与现有token pruning、KV cache等优化方案叠加，在对精度要求高的商品搜索/内容理解场景优先采用全视觉token+算子跳过，比激进剪枝的精度保留效果更好

  - 预算可调的设计可直接作为业务部署的性能-精度旋钮，根据在线流量峰谷动态调整跳过算子数量，平衡资源成本和服务效果'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
多模态大语言模型（MLLM）为保留细粒度视觉信息，视觉token长度可达数千级，prefill阶段推理计算量激增。现有加速方案要么剪枝视觉token导致不可逆的细粒度信息丢失（如OCR、小物体识别失效），要么整层跳过视觉更新，将attention和FFN绑定处理，无法适配每层两类算子的差异化贡献，精度损失难以控制。

### 方法关键点
- 提出answer-observable诊断指标，通过计算视觉token更新对最终输出token的一阶影响，精准识别「更新幅度大但对输出无贡献」的answer-silent冗余计算
- 将Transformer层拆分为attention和FFN两个独立算子，分别计算每层跳过视觉attention、跳过视觉FFN、同时跳过两者的输出风险，识别每层的算子主导性（attention主导/FFN主导/两者均冗余）
- 基于给定计算预算选择低风险层，分别采用仅保留FFN、仅保留attention、完全冻结视觉token三种策略，全程保留全量视觉token，避免不可逆信息损失

### 关键实验
在LLaVA-1.5、Qwen2.5-VL、Qwen3-VL 3个主流开源MLLM架构、10个VQA基准（覆盖OCR、细粒度识别、推理类任务）上测试，对比token pruning、整层跳过等基线方案：在Qwen3-VL上降低33.7% TFLOPs，仅损失0.5%平均性能；相同推理延迟下，精度比整层跳过方案高2~3个百分点，还可与token pruning方案叠加进一步提升效率。

### 最值得记住的结论
MLLM中的视觉冗余并非按token或整层分布，而是算子粒度、层依赖的，仅去除对最终输出无影响的answer-silent计算，可实现最优的效率-精度平衡

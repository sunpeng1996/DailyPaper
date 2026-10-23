---
title: Compiling Autoregressive LLM Control into Policy-Exact Parallel Inference for
  Hierarchical RAG
title_zh: 面向分层RAG的自回归LLM控制编译：策略精确的并行推理
authors:
- Zehao Lin
- Qianfeng Shen
- Xixuan Hao
- Shaobo Cui
- Chunyu Li
- Kai Chen
- Bo Tang
- Zhenjun Wang
- Jin Yan
- Zhiyu Li
affiliations:
- MemTensor (Shanghai) Technology Co., Ltd.
- China Haisum Engineering Co., Ltd.
- The Hong Kong University of Science and Technology (Guangzhou)
- Shanghai Jiao Tong University
arxiv_id: '2610.30664'
url: https://arxiv.org/abs/2610.30664
pdf_url: https://arxiv.org/pdf/2610.30664
published: '2026-10-22'
collected: '2026-10-23'
category: RAG
direction: 分层RAG · LLM控制并行推理优化
tags:
- Hierarchical_RAG
- Parallel_Inference
- Constrained_Decoding
- LLM_Control
- Tree_Attention
one_liner: 将分层RAG有限动作LLM控制器编译为前缀树，2次前向实现串行等价策略，延迟降35%-47%
practical_value: '- 电商/广告RAG的有限动作控制场景（如分层检索选库、工具调用选工具）可直接复用该编译方法，用树因果探针替换串行语法解码，在保策略一致的前提下降30%+延迟，同时完全避免JSON解析错误

  - 当LLM控制器动作空间有限、决策步数≤3时均可使用该方案：仅1次prefill+1次探针前向，完全消除串行解码的关键路径依赖，收益随prompt长度提升

  - 可复用sequential interaction mass指标，量化单步决策与历史依赖决策的效用差，快速判断轻量单步决策的适用场景

  - 策略一致性要求高的场景可复用margin校验逻辑，将决策margin小于阈值的请求fallback到串行解码，兼顾低延迟和核心请求的策略正确性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
分层RAG中LLM作为控制器串行选择文档子树时面临三重矛盾：自由格式JSON解码存在3%-65%的语法/标识错误；单步logit选TopK丢失历史依赖导致决策质量下降；语法约束解码保策略但逐token串行前向延迟高。现有串行执行模式是执行框架的人为产物，而非控制器的必然要求。
### 方法关键点
- 将有限动作、决策步数≤3的控制器动作空间编译为前缀树，仅两步执行：1次root prefill得到首动作logit并缓存公共KV；1次树因果探针前向计算所有可达前缀的logit，每个状态的token、位置ID、注意力掩码和串行解码完全一致，保证策略精确等价
- 证明前缀状态等价引理，精确算术下编译后与串行解码策略100%一致；支持顺序边缘化的MAP集合推理，可精确证明最优选择集，无需截断启发式
- 提出sequential interaction mass指标，量化单步决策和历史依赖决策的KL散度，可bound单步决策的效用损失
### 关键实验
在QASPER数据集4个文档不重叠拆分上测试，采用Qwen2.5-7B/3B模型：编译后与串行解码的动作序列匹配率达84%-89%，所有差异均为浮点精度near-tie导致；控制延迟比逐token串行解码低35%-47%，比理想分块串行引擎低6%-7%；完全消除输出token和协议解析错误；决策步数≤3时收益显著，步数到4时探针宽度爆炸失去优势。
### 核心结论
有限动作、有限horizon的LLM控制器不需要串行解码，编译为前缀树用并行探针执行可在保策略的前提下大幅降低延迟

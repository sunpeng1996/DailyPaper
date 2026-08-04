---
title: 'From Chains to Trees: Parent-Conditioned Drafting for Semi-Autoregressive
  Speculative Decoding'
title_zh: 父条件草稿树PCTree：半自回归推测解码的无训加速方案
authors:
- Zixian Li
- Tong Li
- Chi Xie
- Xiaohui Song
- Haonan Lu
affiliations:
- OPPO AI Center
arxiv_id: '2608.02123'
url: https://arxiv.org/abs/2608.02123
pdf_url: https://arxiv.org/pdf/2608.02123
published: '2026-08-03'
collected: '2026-08-04'
category: LLM
direction: LLM推理优化 · 推测解码加速
tags:
- Speculative Decoding
- LLM Inference
- Semi-Autoregressive
- Tree Decoding
- DSpark
- Inference Optimization
one_liner: 无需重训将半自回归推测解码的链式草稿转为树状，提升LLM推理加速比
practical_value: '- 现有DSpark部署可零训练成本升级：仅修改推理候选生成逻辑，无需重训模型，即可获得7.5%~29.5%的LLM推理加速收益，适合文案生成、客服回复、推荐理由生成等大流量LLM场景

  - Agent落地优化参考：在低延迟要求的实时Agent交互场景中，默认参数k=4、N=32为跨任务通用最优工作点，无需逐场景调参即可有效降低LLM调用延迟

  - 工程复用思路：半自回归+轻量条件头的架构可直接扩展树状解码，对于已上线推测解码的业务，仅需调整候选剪枝和验证打包逻辑即可迁移，落地成本极低'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
半自回归推测解码方法DSpark通过一次并行骨干前向生成整段token块，大幅降低了草稿生成延迟，但其仅输出单条线性草稿，若前缀token验证失败则整块后缀全部作废，块越大浪费越严重，限制了加速比上限；现有树状推测解码方案要么需要多轮草稿前向，要么要求重训模型，落地成本高。

### 方法关键点
- 完全复用DSpark预训练的并行骨干与轻量Markov头，无需额外训练、无新增骨干前向开销
- 每层批处理当前所有父节点调用Markov头，生成父条件专属的子节点概率，避免无父条件拼接的路径不一致问题
- 每层保留top-k最高联合概率节点作为扩展边界，全局筛选top-N节点组成待验证树，一次目标模型前向完成全树验证

### 关键实验
在Qwen3-{4B/8B/14B}三个模型、GSM8K/MBPP/MT-Bench等9个基准上测试：B=7时相对DSpark的AR解码加速比提升3.1%~29.5%；B=16时Qwen3-4B在GSM8K上平均接受长度从9.41升至11.16，AR加速比从6.14×提升至6.60×，块越大增益越显著。

### 核心结论
半自回归草稿的并行骨干+顺序细化架构天然支持树状扩展，仅通过推理策略修改即可获得显著加速收益，无任何训练成本。

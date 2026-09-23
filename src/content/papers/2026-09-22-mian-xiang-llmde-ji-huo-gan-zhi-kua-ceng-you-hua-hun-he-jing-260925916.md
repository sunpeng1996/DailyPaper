---
title: 'Beyond Scalar Sensitivity: Activation-Aware Mixed-Precision LLM Quantization
  with Cross-Layer Refinement'
title_zh: 面向LLM的激活感知跨层优化混合精度量化方法CASA
authors:
- Akihiro Yoshida
- Yuma Ichikawa
affiliations:
- Fujitsu Limited
- Institute of Science Tokyo
- RIKEN Center for AIP
arxiv_id: '2609.25916'
url: https://arxiv.org/abs/2609.25916
pdf_url: https://arxiv.org/pdf/2609.25916
published: '2026-09-22'
collected: '2026-09-23'
category: LLM
direction: LLM推理优化 · 混合精度量化
tags:
- Quantization
- Mixed-Precision
- LLM
- Post-Training Quantization
- Hessian
- Cross-Layer Optimization
one_liner: 提出两阶段CASA混合精度量化方案，突破标量敏感代理限制，实现超低位宽下LLM低损失压缩
practical_value: '- 电商/推荐场景部署轻量化LLM（如端侧推荐Agent、客服大模型）时，可直接复用CASA两阶段量化方案，在<3bit超低位宽下最小化精度损失，降低推理硬件成本

  - 给LLM模块分配计算/存储资源时，可替换传统标量敏感度指标，采用基于Kronecker分解Hessian的激活感知度量，避免给早期层V投影等高敏感模块分配过少资源导致效果暴跌

  - 多模块资源分配场景（如召回排序链路算力调度、多Agent任务资源分配）可借鉴「单模块最优解初始化+跨模块局部搜索调优」的两阶段思路，比直接求解带跨项的整数规划效率更高、效果更好'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有混合精度量化的MCKP求解依赖标量敏感代理，丢弃Hessian方向信息且假设层间独立，导致高敏感模块比特分配不足。理论证明标量代理的失真上限为√(κ(A)κ(B))，实际LLM模块该值跨度达10^1~10^13，层间敏感度排序完全不可靠，超低位宽下精度损失严重。

### 方法关键点
- 两阶段CASA架构：Stage1用基于Kronecker分解Hessian的激活感知度量替代标量代理，求解MCKP得到初始比特分配，连续松弛下存在闭式解
- Stage2基于相邻层交叉项的上界代理做贪心比特交换局部搜索，用端到端校准损失判断更新是否接受，天然覆盖层间误差传播影响，且解不会劣于Stage1结果

### 关键结果
在Llama2/3、Qwen3系列7B~14B模型上测试，对比Uniform、Q-Palette等基线：2.25~2.75bit超低位宽下，Llama3-8B的WikiText-2困惑度比Q-Palette低52%，6任务零样本准确率高5.2pct；Qwen3-14B在2.25bit下准确率比Q-Palette高7.2pct，性能增益和模型平均标量失真边界正相关。

### 核心结论
标量敏感度代理的失真上限可超10^10，混合精度资源分配必须考虑激活分布各向异性和跨层交互，两阶段求解远优于直接整合跨项的单阶段整数规划

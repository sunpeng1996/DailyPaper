---
title: 'LoGo: Token-Level Dynamic Local-Global Attention'
title_zh: LoGo：Token级动态调度的局部-全局注意力机制
authors:
- Yuqi Pan
- Zheng Li
- Bohao Tang
- Zhen Qin
- Guoqi Li
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- ByteDance Seed
arxiv_id: '2608.29539'
url: https://arxiv.org/abs/2608.29539
pdf_url: https://arxiv.org/pdf/2608.29539
published: '2026-08-30'
collected: '2026-09-01'
category: LLM
direction: 大模型优化 · 长上下文注意力
tags:
- Attention
- Long Context
- Dynamic Routing
- Inference Efficiency
- Triton Kernel
one_liner: 通过token级动态路由选择是否激活全局注意力，相同计算预算下提升长上下文大模型性能
practical_value: '- 可将token级动态路由思路迁移到长用户行为序列的推荐召回/排序场景，仅对需要长依赖的item/用户特征激活全局注意力，降低长序列建模开销

  - 阈值控制+渐进式掩码的训练策略可直接复用在各类动态路由任务中，无需辅助损失即可稳定控制路由比例，避免冷启动阶段信号不稳定问题

  - query-sparse Triton kernel的实现思路可复用在大模型推理服务中，针对电商/广告场景的长prompt（如用户全行为序列）动态裁剪计算量，提升推理速度

  - 若业务使用静态局部-全局混合注意力基座，可直接将全局注意力层替换为LoGo层，在不增加内存开销的前提下提升长上下文性能'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长上下文大模型中，标准Transformer对所有token均匀分配全局注意力计算资源，静态局部-全局混合注意力不考虑token的上下文依赖需求，导致全局计算浪费在局部可预测的token上，长上下文性能与计算效率的trade-off难以优化。

### 方法关键点
- 每层设置耦合的局部、全局注意力分支：局部分支处理所有token的固定窗口（实验用128）注意力，全局分支仅对选中token开放全上下文访问；分支通过轻量线性变换共享主QKV参数，仅增加约1%参数量
- 新增token级门控预测全局注意力偏好，通过自适应阈值控制全局激活比例，无需辅助损失即可稳定维持预设的全局计算预算
- 设计渐进式掩码（P-mask）训练策略：初始阶段所有token激活全局注意力，逐步提升阈值引入稀疏路由，避免训练初期路由信号不稳定导致的收敛问题
- 实现query-sparse Triton kernel，仅对选中的query计算全局注意力，将FLOPs节省转化为实际运行速度提升

### 关键实验结果
在200M~3.3B参数规模下验证，与全注意力Transformer相比，相同计算资源下保持一致的缩放规律；1.5B参数、50%全局预算配置下，长程检索任务RULER-32k平均得分达83.0，比全注意力Transformer高4.1，比最优静态混合方案高7.2；64k序列长度下50%全局预算的推理速度比FlashAttention快1.99倍。

最值得记住的结论：全局注意力的计算资源应该花在真正需要长程依赖的token上，动态token级资源分配比静态分层/分头分配的效率更高。

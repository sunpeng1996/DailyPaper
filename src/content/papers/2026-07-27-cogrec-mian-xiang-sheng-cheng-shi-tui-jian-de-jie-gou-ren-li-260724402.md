---
title: 'CogRec: Structure-Cognitive Fast-and-Slow Reasoning for Generative Recommendation'
title_zh: CogRec：面向生成式推荐的结构认知快慢推理框架
authors:
- Xiang Liu
- Jingsong Su
- Shuqi Zhao
- Pengbo Mo
- Yiming Qiu
- Huimu Wang
- Mingming Li
- Jiao Dai
- Jizhong Han
- Songlin Hu
affiliations:
- Chinese Academy of Sciences
- Beijing Normal University
- JD.com
- University of Chinese Academy of Sciences
arxiv_id: '2607.24402'
url: https://arxiv.org/abs/2607.24402
pdf_url: https://arxiv.org/pdf/2607.24402
published: '2026-07-27'
collected: '2026-07-28'
category: GenRec
direction: 生成式推荐 · Semantic ID结构推理
tags:
- Generative Recommendation
- Semantic ID
- Fast-and-Slow Reasoning
- Sequential Recommendation
- SID Routing
one_liner: 基于Semantic ID拓扑设计结构感知快慢推理路由，解决生成式推荐推理预测对齐问题
practical_value: '- 做Semantic ID生成式推荐时，可复用SID拓扑扩展方案：在原有层级SID基础上补充层内语义图+商品级邻接索引，把输出格式转化为可推理的导航空间，提升推理与生成的对齐度

  - 多阶段训练范式可直接复用：先对齐SID token语义，再训练直接生成基线，最后基于同一checkpoint训不同推理分支，可控对比不同推理策略的效果，降低迭代成本

  - 可参考难易度分层规则（基于历史与目标的SID前缀匹配度+层内图距离）对请求路由：简单请求走直接生成省算力，中等难度请求走SID Routing提效果，难请求补召回池兜底

  - 训练时将用户历史中的SID token也纳入损失计算，比仅计算输出侧损失更能提升SID表征一致性，生成准确率更高'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于Semantic ID的生成式推荐仅把SID当待记忆的目标序列，层级结构、层内关联、商品邻域都未被用作显式推理空间；而带自然语言推理的生成式推荐存在推理空间（文本）和预测空间（SID离散空间）不匹配的问题，推理和最终生成的SID弱耦合，效果提升有限。

### 方法关键点
- 重构结构认知型SID拓扑：在原有层级SID基础上，补充每层编码中心的语义关联图，再加商品级HNSW邻接索引，把纯输出的SID树改造成可导航的推理拓扑
- 定义SID Routing三类快慢推理操作：`Match`（快速语义定位，同层SID码匹配，成本0）、`LateralJump`（层内语义边跳转，中速，成本1）、`Explore`（无直接边的探索，慢速，成本2），基于历史与目标SID的关联自动生成路由路径作为监督信号
- 多阶段可控训练pipeline：Stage0 建SID拓扑+扩展词表；Stage1 冻结LLM参数仅对齐新增SID token语义；Stage2 训练直接生成目标SID的基线模型；Stage3 基于同一基线checkpoint分别训自然语言推理分支和SID Routing推理分支，保证变量仅为推理形式

### 关键结果
在Amazon Beauty、Sports、Toys三个公开序列推荐数据集上对比三类基线：SID Routing在Sports数据集上NDCG@10达0.0274，比直接生成基线提升7%；在Medium难度样本（前缀匹配不足但存在可学习SID关联）上效果提升最明显，比自然语言推理的Hit@10最高提升17.9%；但在Easy样本上直接生成效率和效果更优，Hard样本所有方法表现都较差。

最值得记住的结论：生成式推荐的推理模块只有和目标SID的结构空间对齐才能真正发挥作用，并非越长越复杂的推理效果越好。

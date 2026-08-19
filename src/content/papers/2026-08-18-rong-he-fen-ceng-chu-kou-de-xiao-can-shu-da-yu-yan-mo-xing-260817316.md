---
title: Empowering Compact LLMs with Fusion of Layer-wise Exits for Recommendation
title_zh: 融合分层出口的小参数大语言模型推荐增强框架FLEXRec
authors:
- Xurong Liang
- Tong Chen
- Quoc Viet Hung Nguyen
- Jianxin Li
- Xiangliang Zhang
- Hongzhi Yin
affiliations:
- The University of Queensland
- Griffith University
- Edith Cowan University
- University of Notre Dame
arxiv_id: '2608.17316'
url: https://arxiv.org/abs/2608.17316
pdf_url: https://arxiv.org/pdf/2608.17316
published: '2026-08-18'
collected: '2026-08-19'
category: RecSys
direction: LLM推荐 · 小参数模型性能优化
tags:
- Sequential Recommendation
- Compact LLM
- Layer-wise Exits
- Adaptive Routing
- MoE
- LoRA
one_liner: 针对小参数LLM推荐精度不足问题，提出动态分层出口融合框架FLEXRec，兼顾精度与推理效率
practical_value: '- 可直接在现有小参数LLM推荐底座上叠加分层出口设计，仅新增每层轻量预测头，无需修改LLM主干结构，改造成本极低

  - 三阶段训练范式可复用：先通过LoRA微调基础推荐能力，再单独预热中间层出口，最后仅训练路由矩阵，计算开销远低于全量重训LLM

  - target-k hinge loss+连续ReLU路由可直接替代传统固定Top-k路由，支持按用户序列复杂度自适应调整计算量：简单序列少激活层降延迟，复杂序列多层融合提精度，实测额外延迟不到1ms，适配线上实时推荐要求

  - 若业务对成本敏感，可训练多套不同target-k的路由共享同一LLM底座，分别适配端侧、服务端等不同算力约束的部署场景'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM推荐系统面临落地两难：大参数模型推理成本过高难以支撑大规模全库排序，小参数模型语义表达能力不足导致推荐精度偏低。传统小模型增强方案（知识蒸馏、CoT推理等）要么需额外维护大模型教师，要么推理延迟飙升，且生成式推荐的自回归解码无法满足高吞吐排序需求；而主流判别式LLM推荐仅依赖最后一层输出，完全浪费不同层捕获的多粒度语义信息，也无法适配不同复杂度的用户行为序列，亟需兼顾精度、效率与落地成本的优化方案。
### 方法关键点
- 架构改造：在LLM每个Transformer层后新增预测头作为出口，利用浅层捕获的短期行为模式、深层捕获的长期用户意图，融合多层预测结果补偿小模型容量不足的问题
- 动态路由：设计AC-Router自适应连续路由，基于用户序列特征动态选择激活的出口集合，推断时仅前向传播到最深激活层即可停止，避免无效计算
- 优化目标：提出target-k hinge loss，搭配负载均衡损失、Z-loss联合优化路由，既保证激活层数控制在预设范围内，又避免路由坍塌、混合精度训练数值不稳定问题
- 低本训练：采用三阶段训练流程，先LoRA微调基础推荐底座，再预热中间层出口，最后仅训练路由投影矩阵，训练成本极低
### 关键实验
在Toys、Beauty、Yelp三个公开电商/本地生活数据集上测试，以E4SRec等SOTA判别式LLM推荐为基线，采用Qwen 3 1.7B、Llama 3.2 3B小参数底座，NDCG@20最高提升6.7%，推理额外开销不到1ms，部分场景精度甚至超过4B/8B大参数LLM基线。
### 核心结论
小参数LLM的中间层语义信息是未被充分利用的免费性能增益，动态分层融合是兼顾推荐精度与推理效率的高性价比落地路径

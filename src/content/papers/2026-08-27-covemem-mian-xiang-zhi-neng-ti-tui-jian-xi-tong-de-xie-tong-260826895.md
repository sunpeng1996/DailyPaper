---
title: 'When Memory Takes Gradients: Collaborative Vector Memory for Agentic Recommender
  Systems'
title_zh: CoVeMem：面向智能体推荐系统的协同向量记忆机制
authors:
- Hanchong Chen
- Xing Tang
- Lingjie Li
- Xiongfeng Shan
- Xiuqiang He
affiliations:
- Shenzhen Technology University
arxiv_id: '2608.26895'
url: https://arxiv.org/abs/2608.26895
pdf_url: https://arxiv.org/pdf/2608.26895
published: '2026-08-27'
collected: '2026-08-28'
category: Agent
direction: 智能体推荐 · 协同向量记忆
tags:
- CoVeMem
- Agentic Recommendation
- Vector Memory
- LoRA
- LightGCN
- Contrastive Learning
one_liner: 提出协同向量记忆CoVeMem，无需额外LLM调用维护记忆，性能超越文本记忆智能体
practical_value: '- 可复用「传统协同模型embedding+projector映射为soft token注入LLM」的架构，省去文本记忆蒸馏、逐次更新的大量LLM调用成本，适合高并发电商推荐场景

  - 训练阶段直接复用「候选标题随机掩码+listwise损失」的trick，强制LLM学习协同向量信号，避免文本捷径，可迁移到所有融合协同信号与LLM的推荐任务

  - 推理阶段用pointwise yes/no readout替代生成式排序，既降低上下文长度压力，又避免生成结果解析错误，大幅提升推理稳定性

  - 历史交互检索可放弃默认的时序截断，改用候选集合向量质心检索最相关的历史交互，能有效提升历史信号的利用率'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前Agent推荐系统普遍采用文本格式记忆，存在两处核心瓶颈：一是每次更新记忆都需要调用LLM重写，维护成本极高，无法高效利用全量用户交互历史；二是文本序列化会损失全局协同结构信息，无法保留全品类的用户偏好相似度，且排序梯度无法直接更新文本记忆，限制推荐效果上限。
### 方法关键点
- 记忆库：用LightGCN预训练生成冻结的user、item向量作为协同记忆库，仅保留轻量用户文本profile，无需后续LLM调用更新记忆
- 候选感知检索：每次决策时以候选集合的向量质心为query，从用户历史交互中检索Top-K最相关的向量，而非直接取最近交互
- 模态对齐：用门控MLP将协同向量映射为LLM可接受的soft token，先通过物品文本语义锚的对比损失完成模态对齐，再用LoRA微调LLM适配协同token
- 训练&推理优化：训练阶段随机掩码候选标题，用masked listwise损失强制模型学习使用协同信号，避免依赖文本捷径；推理阶段用pointwise yes/no读-out打分，降低推理成本
### 关键结果
在InstructRec的4个公开基准数据集上测试，对比MemRec等最强文本记忆智能体基线，在20个指标单元中的19个持平或超越；在交互稠密的Goodreads数据集上Hit@1从0.3087提升至0.7730，同时完全省去记忆维护的额外LLM调用，推理token成本为所有对比方法最低。
### 核心结论
Agent推荐的记忆载体不必局限于文本，传统协同模型产出的向量作为可梯度训练的记忆，既能保留完整协同信号，还能大幅降低系统成本。

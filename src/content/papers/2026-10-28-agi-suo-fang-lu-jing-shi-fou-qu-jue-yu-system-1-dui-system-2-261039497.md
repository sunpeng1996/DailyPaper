---
title: Does Scaling Toward AGI Depend on What System-1 Lets System-2 Execute?
title_zh: AGI 缩放路径是否取决于 System-1 对 System-2 执行任务的筛选
authors:
- Qi Wang
- Yun Qu
- Lizhou Cai
- Heming Zou
- Haoang Chi
- Yiqin Lv
- Xiang Li
- Haiyan Feng
- Mengyu Ge
- Yize Geng
affiliations:
- 清华大学自动化系
- 清华大学计算机科学与技术系
arxiv_id: '2610.39497'
url: https://arxiv.org/abs/2610.39497
pdf_url: https://arxiv.org/pdf/2610.39497
published: '2026-10-28'
collected: '2026-11-02'
category: Agent
direction: Agent系统架构 · 双系统协同设计
tags:
- System-1
- System-2
- Conditional Interaction
- Co-Design
- Scaling Efficiency
- AGI
one_liner: 提出轻量System-1与重资源System-2协同设计的条件交互框架，大幅提升AGI缩放的资源利用效率
practical_value: '- 生成式推荐/电商Agent场景可部署双级路由：用LoRA微调的轻量小模型做System-1，预评分候选query、工具调用、CoT推理路径，仅超过阈值的请求调用大模型System-2执行，实测可降低30%~70%推理成本

  - 模型训练阶段复用条件交互框架筛选样本：用轻量模型预估每个训练样本的信息增益，仅保留高价值样本做RLHF/GRPO训练，既能降低训练成本，还可加快收敛速度

  - 可直接复用阈值自适应更新公式，根据实时准入率动态调整筛选阈值，平衡效果与成本，适配业务预算波动、流量峰谷变化的场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前AGI缩放主要依赖堆叠System-2（重资源的推理、规划、执行模块）的参数量、训练数据与算力，但无差别执行所有交互（如CoT推理、工具调用、训练rollout）的边际收益快速下降，大量资源被浪费在无信息增益的低价值交互上，成为下一代AI系统缩放的核心瓶颈。
### 方法关键点
1. 提出条件交互的predict-gate-execute-update闭环：轻量语义感知的System-1预估候选交互的效用，仅筛选高于自适应阈值的高价值交互交由System-2执行，执行结果回传用于迭代优化System-1
2. 定义效用相关交互密度$\rho_u$作为缩放效率核心度量，提出用有效算力（informative compute）替代总算力作为更科学的缩放评价指标
3. 给出双系统协同落地方案：包含候选表征、效用预测、动态门控、反馈更新4个模块化组件，支持静态级联、自适应联合优化两种部署模式
4. 推导理想场景下算力节省上限为$1/\rho_u$，同时给出预测误差、探索需求、分布偏移场景下的收益衰减边界与选择后悔上界
### 关键结果
理想筛选、执行成本一致的条件下，执行算力可降低至原有水平的$1/\rho_u$；已有的RLVR训练场景落地验证，该框架可实现数倍的rollout成本节省，同时不损失模型收敛效果。

**最值得记住的结论**：未来AGI缩放的核心瓶颈不再是总算力规模，而是有多少算力被投入到了真正有价值的交互上

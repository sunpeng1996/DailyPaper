---
title: 'Every Ablation Is a Dose: Counterweights and the Semblance of Self-Repair'
title_zh: 每次消融都是一次剂量干预：平衡权重与自修复现象的本质
authors:
- Areeb Ahmad
- Pratinav Seth
- Vinay Kumar Sankarapu
affiliations:
- Lexsi Labs
arxiv_id: '2610.02173'
url: https://arxiv.org/abs/2610.02173
pdf_url: https://arxiv.org/pdf/2610.02173
published: '2026-10-01'
collected: '2026-10-02'
category: LLM
direction: LLM机制解释 · 自修复与消融校准
tags:
- Mechanistic_Interpretability
- Ablation
- Self_Repair
- Causal_Intervention
- Counterweights
one_liner: 揭示大模型自修复本质是预存权重耦合，提出剂量轴量化消融与干预效果
practical_value: '- 做LLM4Rec/Agent的消融评估时，可采用连续剂量轴替代传统零/均值/重采样消融，避免自修复效应导致的组件重要性低估，提升推荐路由、工具调用模块的归因准确性

  - 做LLM推理steering（如推荐场景的用户偏好控制、电商内容合规约束）时，可通过上下游单元权重对齐度zr预判耦合强度，大幅降低核心控制单元的筛选成本

  - 搭建电商商品信息校验、评价真伪判断等fact-check类轻量应用时，可直接定位预训练自带的真值编码核心神经元，无需微调即可快速实现核心逻辑'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
消融是大模型可解释性、归因、遗忘评估的核心工具，但自修复效应会导致被消融组件的功能被其他单元补偿，严重低估组件真实贡献，过往研究普遍认为自修复无统一机制，消融结论的可靠性缺乏支撑。
### 方法关键点
- 定义连续剂量λ轴，将所有传统消融方法统一为该轴上的无校准离散点：λ=+1对应原始激活，λ=0对应类中性激活，λ=-1对应反事实激活
- 设计嵌套反事实干预流程：先对上游核心单元施加指定剂量的干预，再测量下游单元对最终结果的贡献变化
- 提出下游单元贡献的仿射定律：$E_r(\lambda) = own_r + \gamma_r\lambda$，$\gamma_r<0$为平衡权重（反向响应核心干预），$\gamma_r>0$为中继（同向响应核心干预）
- 定义静态权重对齐度$z_r$，仅通过模型checkpoint即可预判$\gamma_r$的量级
### 关键结果
在Known-Facts合成的真假陈述判断任务上，覆盖Gemma、Qwen、LLaMA、Mistral四个不同家族的7-9B指令微调模型，以及GPT-2 Small的IOI电路：81个可达下游方向中68个符合仿射定律，其中52个为平衡权重；用3个剂量点拟合的模型预测留出的半剂量点，out-of-sample $R^2$达0.65~0.91；静态权重对齐度$z_r$与$|\gamma_r|$的Spearman相关系数达0.55~0.82；传统零/均值消融的实际剂量由数据决定，不同样本的干预强度差异极大。
### 核心结论
大模型自修复不是动态产生的补偿机制，而是预训练阶段已存在的平衡权重耦合的被动释放。

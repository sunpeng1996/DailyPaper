---
title: 'Omni-Decision: Evidence-Ledger Planning for Omni-Modal Agents'
title_zh: Omni-Decision：面向全模态Agent的证据账本规划框架
authors:
- Ming Ma
- Yi Zhu
- Yiran Zhong
- Feida Zhu
- Yuhao Wang
- Junhan Shi
- Lingrui Mei
- Tianming Yang
- Steven Hoi
affiliations:
- Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Alibaba Tongyi Lab
- Shanghai Jiao Tong University
- Tsinghua University
arxiv_id: '2607.11433'
url: https://arxiv.org/abs/2607.11433
pdf_url: https://arxiv.org/pdf/2607.11433
published: '2026-09-23'
collected: '2026-09-30'
category: Agent
direction: 全模态Agent · 规划能力优化
tags:
- Omni-modal Agent
- Planning
- Evidence Ledger
- Context Management
- Multi-step Reasoning
one_liner: 提出证据账本规划替代累积对话历史，解决全模态Agent规划瓶颈，精度SOTA且成本仅Gemini 3.1 Pro的43%
practical_value: '- 全模态导购/直播内容理解Agent可直接复用证据账本架构：将多轮商品搜索、属性爬取、直播/短视频内容识别结果结构化存入账本，避免对话历史累积噪声导致的决策错误，同时降低长任务推理的上下文token开销

  - Agent训练可复用无标注轨迹训练范式：直接用运行过程中记录的账本状态、动作、判决结果做SFT和决策层RL，无需人工标注每一步监督信号，大幅降低小模型Agent能力迭代的标注成本

  - 多模块Agent架构优化可参考核心结论：规划模块的性能对整体效果的影响远大于感知模块，资源投入应优先倾斜规划层优化，而非盲目升级多模态感知模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
全模态Agent需要跨视频、音频、网页、计算工具多源获取证据回答复杂问题，现有方案存在两大核心痛点：一是多模态观测噪声大，累积在对话历史中会严重干扰后续规划决策，导致提前收敛或动作不合理；二是当前多模态模型的能力短板集中在规划层，控制变量实验验证替换规划器带来的性能下降远高于替换感知后端，规划是全模态Agent的核心瓶颈。
### 方法关键点
- 核心设计**证据账本**：每个任务维护结构化账本，包含未解决证据需求U、已确认事实/计算结果F、带来源的确认证据E、未解决冲突C四个字段，替代持续增长的对话历史作为规划的唯一持久上下文
- 引入独立critic模块：针对每个新观测仅提取可用有效内容提交给账本，丢弃噪声信息，保证规划上下文始终紧凑无冗余
- 无标注训练范式：执行过程中自动记录每一步的状态、动作、判决结果，无需人工标注，直接基于正确轨迹做SFT，再用闭合度对齐的RL优化规划器决策能力
### 关键实验
在OmniGAIA全模态基准上达到81.4%的SOTA精度，单问题推理成本仅为Gemini-3.1-Pro的43%；在WorldSense长视频理解基准上精度达65.0%，与当前最强端到端模型持平；控制变量实验显示替换规划器带来的精度下降是替换感知模块的1.5倍，比无账本的ReAct方案整体精度高21个百分点。
### 核心结论
全模态Agent的核心瓶颈是规划而非感知，规划层优化的投入产出比远高于感知层升级

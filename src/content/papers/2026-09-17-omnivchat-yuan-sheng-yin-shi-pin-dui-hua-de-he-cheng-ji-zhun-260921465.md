---
title: 'OmniVChat: Synthesizing, Benchmarking, and Training for Native Audio-Visual
  Dialogue'
title_zh: OmniVChat：原生音视频对话的合成、基准构建与训练框架
authors:
- Haolin He
- Yunfei Chu
- Qi Chen
- Wen Huang
- Yuan Feng
- Muzhi Zhu
- Zheqi Dai
- Haoning Xu
- Dongchao Yang
- Chunyat Wu
affiliations:
- The Chinese University of Hong Kong
- Alibaba Group
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
- Zhejiang University
arxiv_id: '2609.21465'
url: https://arxiv.org/abs/2609.21465
pdf_url: https://arxiv.org/pdf/2609.21465
published: '2026-09-17'
collected: '2026-09-21'
category: Multimodal
direction: 多模态音视频对话 · 多Agent数据合成
tags:
- MultiAgent
- Multimodal Dialogue
- Synthetic Data
- Reinforcement Learning
- Benchmark
- LoRA
one_liner: 提出多Agent数据合成引擎、分级评测基准与多目标RL训练方案，优化原生音视频对话能力
practical_value: '- 多Agent数据合成架构可复用：参考Director/Renderer/Reviewer/Validator四角色分工，低成本生成电商场景多模态交互数据（如直播带货用户提问、商品展示对话），解决真实标注数据不足问题

  - 分级rubric评测方法可迁移到生成式推荐/多模态客服效果评估：采用分层通关式打分规则（基础门槛→内容正确→风格匹配），配合大模型自动判分，替代人工做批量效果验收，降低评估成本

  - 多目标RL reward设计可复用：将正确性、效率、风格拆分为独立可调节的reward项，在电商客服、直播话术生成场景中，可根据业务需求调整权重，平衡回复准确率、简洁度、口语化风格的优先级'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
原生音视频对话无需额外ASR、字幕等预处理步骤，可降低延迟、保留完整感知 cues，是下一代实时交互Agent（如电商直播智能助理、线下导购数字人）的核心能力，但当前面临两大瓶颈：一是真实原生音视频对话数据稀缺，二是开放域回复质量难以用规则化方法评估，制约了相关模型的落地优化。

### 方法关键点
- 数据层：提出OmniVChat-Studio多Agent数据引擎，通过Director（文案生成）、Renderer（音视频渲染）、Reviewer（内容校验）、Validator（规则校验）四角色协作，可规模化生成单/多轮原生音视频对话数据，自动配套参考回复和分级评测rubric
- 评测层：构建OmniVChat-Bench基准，覆盖5大类能力、17个子类别、22个场景，采用分层通关式打分规则：Tier 0为语言正确性门槛，不达标直接得0分，更高层级得分依赖所有低层级要求全部满足，使用大模型自动判分
- 训练层：提出OmniVChat-RL多目标强化学习框架，reward包含正确性（和评测用相同rubric得分）、格式合规性、回复效率（单位字数得分密度）、风格匹配度四个维度，使用LoRA对Qwen3-Omni做轻量微调

### 关键实验
训练集为5600条合成对话，测试集包含2800条合成基准数据、360条真实人类录制对话。微调后模型在合成基准上得分从0.465提升至0.652，在真实数据上得分从0.402提升至0.632，回复平均长度从91.5词降至36.6词，回复效率（每千词得分）从3.37提升至17.18，风格符合率从0.71提升至0.992，效果超过多数开源及部分闭源多模态大模型。

### 最值得记住的一句话
高质量合成数据配合对齐的评测规则与RL训练，可以实现和真实数据训练相当的效果，大幅降低多模态交互模型的落地成本

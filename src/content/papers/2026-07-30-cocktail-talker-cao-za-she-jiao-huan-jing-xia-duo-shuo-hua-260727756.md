---
title: 'Cocktail-Talker: Multi-Speaker Dialog Modeling in Noisy Social Environments
  with Turn Action GRPO'
title_zh: Cocktail-Talker：嘈杂社交环境下多说话人口语对话建模框架
authors:
- Xilin Jiang
- Riki Shimizu
- Sukru Samet Dindar
- Junkai Wu
- Zhongweiyang Xu
- Nima Mesgarani
affiliations:
- Columbia University
- University of Washington
- University of Illinois Urbana-Champaign
arxiv_id: '2607.27756'
url: https://arxiv.org/abs/2607.27756
pdf_url: https://arxiv.org/pdf/2607.27756
published: '2026-07-30'
collected: '2026-08-01'
category: Agent
direction: 多模态Agent · 复杂环境对话决策
tags:
- Speech-LLM
- GRPO
- Turn-Taking
- Multi-Party-Dialog
- LoRA
one_liner: 基于动作令牌与GRPO训练的语音LLM，可在多说话人嘈杂场景自主决策是否回应
practical_value: '- 多角色对话场景可复用「动作令牌」设计：对应电商客服/用户/商家多方会话场景，Agent可新增<|respond|>/<|skip|>等专用令牌，简化多轮决策建模

  - 低资源场景可借鉴Cocktail-DialogGen数据生成思路：通过LLM模拟场景+TTS合成+噪声混入的pipeline，快速生成大量多模态训练样本，降低真实数据采集成本

  - 分类决策类LLM微调可复用SFT+GRPO的训练范式：先SFT学基础规则，再用GRPO强化决策准确性，比单纯SFT最高提2.5pp准确率，且不降低生成内容质量

  - 噪声鲁棒性优化可参考训练时随机丢弃属性的trick：训练时按概率随机丢弃输入侧的用户/角色属性，提升推理时缺失元数据场景的泛化能力'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
现有口语对话系统大多设计为安静环境下的一对一交互，无法适配真实嘈杂社交场景中多说话人共存、话语并非都指向助手的情况，不仅要决策说什么，还要先决策要不要说，现有方案缺乏对该场景的系统性支持。

### 方法关键点
- 设计3个专用动作令牌：<|respond|>（生成回应）、<|listen|>（静默持续关注）、<|ignore|>（静默忽略无关内容），模型输出先选动作令牌，仅选<|respond|>时才生成后续回应内容
- 构建Cocktail-DialogGen数据生成pipeline：先由Gemini 3 Pro生成多场景多角色对话日志，再用Qwen3-TTS合成各说话人语音，最后按不同SNR混入背景噪声生成训练样本，共生成1280小时训练数据
- 训练分为两阶段：第一阶段基于Qwen2.5-Omni-7B用LoRA做SFT，仅微调Transformer全连接层和新增令牌的嵌入/输出层；第二阶段用GRPO强化学习优化，奖励由动作准确率+格式合规性两部分组成

### 关键结果
对比Moshi、PersonaPlex、Qwen系列、Kimi-Audio等主流语音LLM，在见过/未见过环境下，Cocktail-Talker(SFT+GRPO)的二分类（回应/静默）F1-macro分别达到0.928、0.930，比单纯SFT提升2.5pp，远高于基线最高0.521的水平；回应质量上penalized METEOR在见过环境达到0.194，比基线最高提升0.073，且GRPO优化不会降低条件回应质量；鲁棒性表现优异，SNR低至0-6dB时动作准确率降幅极小，未见过环境仅比见过环境降0.002pp F1-macro。

对需要在多角色复杂场景做决策的LLM来说，先通过专用令牌简化决策空间，再用GRPO强化决策准确率的范式，比直接指令微调的效果提升更显著。

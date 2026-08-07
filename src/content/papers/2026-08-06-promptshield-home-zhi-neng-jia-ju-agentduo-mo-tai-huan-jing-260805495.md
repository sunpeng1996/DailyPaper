---
title: 'PromptShield Home: Ambient Multimodal Prompt Injection Defense for Smart-Home
  Agents'
title_zh: PromptShield Home：智能家居Agent多模态环境提示注入防御框架
authors:
- He Zhang
- Feilong Li
- Dingning Long
- Yilin Cui
- Peijun Zhang
- Yuewen Zhang
- Qianyao Xu
- Xinyi Fu
affiliations:
- The Pennsylvania State University
- Chang'an University
- Beijing Normal University
- Carnegie Mellon University
- Tsinghua University
arxiv_id: '2608.05495'
url: https://arxiv.org/abs/2608.05495
pdf_url: https://arxiv.org/pdf/2608.05495
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: 智能Agent · 提示注入防御
tags:
- Prompt Injection
- MLLM
- Smart Home
- Agent Safety
- Multimodal
one_liner: 构建智能家居环境提示注入基准，验证传统检测器与MLLM互补性，提出路由融合防御方案
practical_value: '- 做LLM/Agent落地安全评估时，不要只看整体准确率，要拆分unsafe-execution rate和safe-completion
  rate两个指标，避免陷入always-block的高准确率陷阱，可直接复用在电商客服Agent、推荐引导Agent的安全评估流程

  - 规则检测器与大模型是互补而非替代关系，可采用「高灵敏度规则触发器+大模型做误报过滤」的架构，平衡安全与体验，适合电商导购Agent敏感指令识别、推荐场景恶意意图过滤等场景

  - 多模态融合不要盲目加模态，ASR、原生音频等模态可能引入噪声或决策不稳定性，需做ablation验证收益后再上线，可用于电商多模态推荐、多模态交互Agent的架构选型'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
智能家居MLLM Agent可直接感知音视频信号，但会误把环境中的电视语音、屏幕文本、旁人对话等非用户指令当做有效请求触发操作，现有方案要么误执行率高要么过度拒绝，且整体准确率指标因标签倾斜（大部分场景无需执行）无法反映真实性能，亟需适配家居场景的提示注入防御框架与评估方法。

### 方法关键点
- 构建PromptShield-Home基准数据集，覆盖收信人歧义、屏幕/音频注入、健康误触发、多人居住、合法指令等6类共19个真实场景，标签包含执行、阻断、询问用户三类
- 设计三层对比框架：L0为传统规则检测器（唤醒词、姿态、OCR）；L1为单MLLM（仅视觉、视觉+ASR、原生音视频三种配置）；L2为多Agent协作（投票、角色专家、跨模型仲裁三种模式）
- 采用拆分指标评估：用unsafe-execution rate（UER，越低越好，衡量非指令场景误执行比例）和safe-completion rate（SCR，越高越好，衡量合法指令执行比例）替代整体准确率，规避标签倾斜带来的评估失真

### 关键结果
在17个动作决策场景（14个无需执行，3个需要执行）上测试：传统检测器L0的UER为100%、SCR为100%；所有单MLLM配置UER≤7.1%但SCR为0%，最优单模型准确率仅76.5%；L0与视觉MLLM的正确集完全不相交，二者的Oracle路由准确率可达94.1%；加入ASR会让MLLM的UER升高到28.6%，原生音视频模型仅会把决策转移到询问用户，无实际收益。

最值得记住的结论：智能家居Agent的安全优化方向是路由融合传统检测器与MLLM的能力，而非用MLLM完全替换传统规则系统

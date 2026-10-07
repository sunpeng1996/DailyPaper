---
title: 'PAIR: Perceptual Affective Inference and Regulation in a Real-Time Multimodal
  Conversational Agent'
title_zh: PAIR：实时多模态对话Agent的感知情感推理与调控框架
authors:
- Kexin Quan
- Zijian Ding
- Jiaye Yong
- Qinshi Zhang
- Dong Wang
- Jessie Chin
affiliations:
- University of Illinois at Urbana-Champaign
- KAIST
- Florida State University
arxiv_id: '2610.07523'
url: https://arxiv.org/abs/2610.07523
pdf_url: https://arxiv.org/pdf/2610.07523
published: '2026-10-05'
collected: '2026-10-07'
category: Agent
direction: 情感支持对话Agent · 多模态交互
tags:
- Conversational Agent
- Multimodal Interaction
- Emotion Regulation
- Longitudinal Deployment
- Affective Computing
one_liner: 提出融合评估推理、跨会话记忆、多模态协同的情感支持对话Agent，14天真实部署验证性能
practical_value: '- 个性化对话类Agent（如电商智能客服、陪伴式导购）可复用150词滚动记忆机制：仅存储高频主题、用户修正、历史交互结果，既降低上下文token消耗，又能提升用户感知的个性化程度

  - 情绪识别场景可参考分场景路由策略：单组件事件走认知评估框架，多组件事件走融合推理框架，相比单一prompt能显著提升识别准确率，可直接用于电商客服情绪预判场景

  - 多模态交互协同设计可直接复用：用统一调控目标同时驱动语音语调、界面颜色、虚拟形象动作，能大幅提升用户感知的共情度，适合直播导购、虚拟客服等场景

  - 线上Agent评估可参考「事件级第一人称反馈」机制，相比离线指标更贴合用户真实体验，可用于优化客服、推荐等场景的满意度评估逻辑'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前情感支持对话Agent普遍存在情绪识别与响应脱节、跨会话上下文缺失、评估依赖离线基准不符合真实使用场景的问题，长期部署的个性化和共情能力不足，难以支撑连续的情感陪伴需求。

### 方法关键点
- 推理层采用双框架路由：单组件情绪事件走认知评估（COG）框架，多组件事件走融合神经推理的COMBINED框架，输出PAD（效价-唤醒度-支配度）情绪指标、可控性等属性，比单一prompt准确率更高
- 调控层基于情绪属性匹配四类调节策略，对话遵循探索-安抚-行动（ECA）流程，最多10轮，统一的调控目标同时驱动语音韵律、环境色、虚拟形象动效的多模态输出
- 跨会话采用滚动记忆机制，每日压缩最近4天的交互上下文、用户修正、调节效果到150词以内，无需梯度更新即可实现个性化适配
- 评估设计：每次对话前后分别做情绪估计，和用户的SAM自评对标，避免数值锚定偏差

### 关键实验结果
14天真实部署19名用户，共1093次会话。情绪识别效价MAE=1.20（9分SAM量表，r=0.68），比无框架LLM基线MAE低0.14，比NRC-VAD词典基线低0.48；支配度MAE=1.30（r=0.54），唤醒度识别准确率较低。初始负面情绪的会话效价平均提升1.34分，两周内用户感知的帮助度提升0.216分，输入长度日均缩短3.4%。

**最值得记住的一句话**：用户感知的理解度和情绪预测的数值误差几乎无关，而是由对话过程中的澄清、共情表达决定。

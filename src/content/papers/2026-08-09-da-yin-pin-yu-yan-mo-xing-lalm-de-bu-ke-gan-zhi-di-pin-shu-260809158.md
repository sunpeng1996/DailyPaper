---
title: 'From Inaudible Inputs to Model Failures: Low-Frequency Safety Risks in LALMs'
title_zh: 大音频语言模型（LALM）的不可感知低频输入安全风险研究
authors:
- Yuanhe Zhang
- Weiliu Wang
- Jie Ren
- Liang Lin
- Zhenhong Zhou
- Haoran Gao
- Kun Wang
- Chen Li
- Li Sun
- Sen Su
affiliations:
- Beijing University of Posts and Telecommunications
- Institute of Information Engineering, Chinese Academy of Sciences
- Nanyang Technological University
- JIUTIAN Research
- Tencent ARC Lab
arxiv_id: '2608.09158'
url: https://arxiv.org/abs/2608.09158
pdf_url: https://arxiv.org/pdf/2608.09158
published: '2026-08-09'
collected: '2026-08-15'
category: Multimodal
direction: 多模态大模型 安全攻防
tags:
- LALM
- Adversarial Attack
- Safety Defense
- Black-box Testing
- Audio Processing
one_liner: 提出黑盒不可感知低频攻击方法ILL与防御方案DRG，揭示LALM未被关注的低频安全风险
practical_value: '- 业务搭载语音交互类Agent（如电商语音导购、语音搜索入口）时，可复用DRG的低频分布偏移检测逻辑，识别不可感知的恶意音频攻击，提升语音交互链路安全性

  - 做语音理解模块的鲁棒性测试时，可借鉴ILL的通用波形模板构造方法，低成本实现黑盒红队测试，提前发现语音输入链路的安全漏洞

  - 涉及多模态输入的搜索/推荐系统，可参考「异常分布检测+二次请求校验」的轻量防御架构，在不显著提升链路耗时的前提下优化异常输入识别能力'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
大音频语言模型（LALM）已广泛应用于各类语音交互场景，但人类无法听到的低频信号仍可被模型音频前端接收，干扰生成结果，该类安全风险此前缺乏系统性的评估方法与防御方案。
### 方法关键点
1. 提出黑盒红队攻击方法ILL：通过句子注意力尺度估计确定有效干扰区间，结合频率混淆迁移构造相位连续的低频攻击波形，人类几乎无法感知。
2. 提出防御方案DRG：检测输入音频的低频分布偏移，识别异常时触发二次录音请求做语义恢复。
### 关键结果
在6款LALM的多类音频理解任务上，ILL可将模型准确率最高降低67个百分点，攻击音频的人类可听度评分均值仅1.33，接近干净音频的1.17；DRG可将受攻击后的模型平均准确率从28.5%提升至重采后的46.1%。

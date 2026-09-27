---
title: Controlling Backchannels in Streamable Full-duplex Models
title_zh: 可流式全双工对话模型中的反馈语（Backchannel）生成控制
authors:
- Maike Züfle
- Peter Polák
- Sefik Emre Eskimez
- Jan Niehues
- Peter Bell
- Ondřej Klejch
affiliations:
- Karlsruhe Institute of Technology
- AppTek
- Charles University
- Sesame AI
- University of Edinburgh
arxiv_id: '2609.29418'
url: https://arxiv.org/abs/2609.29418
pdf_url: https://arxiv.org/pdf/2609.29418
published: '2026-09-24'
collected: '2026-09-27'
category: LLM
direction: 全双工对话模型 · 反馈语可控生成
tags:
- Full-duplex
- Backchannel
- Controllable Generation
- Dialogue Agent
- LLM Extension
one_liner: 为可流式全双工对话模型新增轻量反馈语预测头，实现时机可控的类人短反馈生成
practical_value: '- 智能客服/语音交互Agent可直接复用该轻量预测头方案，无需重训基座即可实现实时反馈语生成，大幅提升对话自然度与用户好感度

  - 阈值可控的触发逻辑可迁移到直播带货AI助手、导购Agent场景，实现不同交互节奏下的实时应答/插话时机自定义

  - 基于基座隐藏态扩展垂直功能的思路可复用在各类垂域LLM优化中，大幅降低小功能定制的训练与部署成本'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
全双工语音对话模型支持同时听说，是实时语音交互场景的核心底座，但现有模型的Backchannel（如“uh-huh”“嗯”这类短反馈）生成是训练副产物，时机不可控，重训或RL优化成本极高，也无法对齐人类真实交互习惯。
### 方法关键点
1. 新增轻量Backchannel预测头，直接复用全双工模型自身输出的隐藏态预测反馈语触发时机，无需额外输入特征；
2. 预测概率超过可调节阈值时强制解码反馈语，支持不同场景自定义触发频率；
3. 无需重训基座模型，可适配1B~7B不同参数量的全双工对话模型，泛用性强。
### 关键结果
探测实验证实基座隐藏态可准确预判人类反馈语时机，生成的反馈语频次更高、时机更准，人类评测显示其效果与真实人类生成的反馈语水平相当。

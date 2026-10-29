---
title: 'Beyond Answer Changes: Matched Same-Class Controls for Local Audio Evidence'
title_zh: 《超越答案变化：面向本地音频证据的匹配同类对照方法》
authors:
- Yunuo Wang
- Maoyuan Chen
- Yuanjin Huang
- Xing Liu
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Wuhan University
- National University of Singapore
- Northeastern University (Toronto)
arxiv_id: '2610.37605'
url: https://arxiv.org/abs/2610.37605
pdf_url: https://arxiv.org/pdf/2610.37605
published: '2026-10-27'
collected: '2026-10-29'
category: Eval
direction: 音频语言模型 · 鲁棒性评估
tags:
- Audio-Language Model
- Model Evaluation
- Robustness Testing
- Waveform Intervention
- Local Evidence
one_liner: 提出匹配同类替换的扰动协议，精准评估音频语言模型对局部事件类别的响应
practical_value: '- 开发带语音交互的电商导购/客服Agent时，可复用同类/异类扰动的对照框架，评估模型对语音输入关键信息的响应是否真实来自音频内容而非先验偏见

  - 做多模态内容推荐鲁棒性评估时，可借鉴「保持语义不变的同类替换」思路，排除内容编辑操作本身对模型输出的干扰，精准度量模型对内容语义的敏感度

  - 语音类搜索Query理解的bad case定位时，可参考该协议设计对照测试，区分误差来自波形识别环节还是语义理解环节'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有音频语言模型扰动评估方法无法区分答案变化是源于局部事件类别变更，还是波形改写本身的干扰，难以判定模型是否真正响应了音频局部语义信息。
### 方法关键点
1. 设计两类匹配的局部音频替换对照：同类替换（替换为同类别音频，理论上答案保持不变）、异类替换（替换为不同类别音频，答案应对应变更），两类替换采用完全相同的时间区间、音量匹配、样本拟合、淡入淡出处理，排除操作变量干扰
2. 基于合成音景和多架构音频模型验证协议有效性
### 关键结果
跨2类架构的3款音频模型、600个合成音景测试：异类替换引发的答案变化率比同类替换高49.7~60.9个百分点；同类替换后模型准确率仅比原始输入低最多5.2个百分点；原始与同类替换回答均正确的试验中，插入类别的音景加权选择准确率达73.7~81.9%

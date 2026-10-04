---
title: 'Multimodal Target Speaker Extraction: Towards Unified Speaker Cues Across
  Modalities'
title_zh: 多模态目标说话人提取：跨模态统一说话人线索研究综述
authors:
- Xinyuan Qian
- Yanghao Zhou
- Ziyang Jiang
- Yu Chen
- Xinjia Zhu
- Xueyan Chen
- Qiquan Zhang
- Zexu Pan
- Jiaying Wang
- Xianghu Yue
affiliations:
- University of Science and Technology Beijing
arxiv_id: '2609.35613'
url: https://arxiv.org/abs/2609.35613
pdf_url: https://arxiv.org/pdf/2609.35613
published: '2026-09-28'
collected: '2026-10-04'
category: Other
direction: 多模态语音处理 · 目标说话人提取
tags:
- Multimodal
- Target Speaker Extraction
- Speech Processing
- Survey
- Foundation Model
one_liner: 系统梳理多模态目标说话人提取技术脉络、数据集与评估方案 指明未来研究方向
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
传统目标说话人提取（TSE）依赖注册语音作为线索，在目标与干扰人声纹相似、同一说话人情感/风格变化、注册语音带噪场景下性能骤降，当前缺少跨模态线索统一梳理的系统性综述。
### 方法关键点
1. 按5类目标区分线索（音频注册、视觉、空间、文本语义、神经线索）分类梳理现有深度学习TSE方案
2. 追踪技术演进路径，覆盖判别式估计器、变分、扩散、流、Codec、基础模型等主流架构
3. 归纳跨模态同步、观测缺失/不可靠、数据稀缺、隐私、计算成本、实时性等落地挑战
### 关键结论
明确自适应线索融合、指令驱动提取、高真实度评估、可信部署4个未来研究方向，完整呈现多模态TSE的技术全景与开放问题。

---
title: 'Sequential Semantic-Non-Semantic Watermarking: Robustness Against UnMarker
  Attacks'
title_zh: 时序语义-非语义混合水印：抵御UnMarker攻击的鲁棒性方案
authors:
- Md Ifraham Iqbal
affiliations:
- Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU)
arxiv_id: '2611.20115'
url: https://arxiv.org/abs/2611.20115
pdf_url: https://arxiv.org/pdf/2611.20115
published: '2026-11-15'
collected: '2026-11-22'
category: Other
direction: AIGC内容治理 · 分层水印防御
tags:
- watermarking
- adversarial robustness
- content provenance
- AIGC governance
- image processing
one_liner: 结合语义与非语义互补水印构建分层防御，提升UnMarker单阶攻击下的水印留存率
practical_value: '- 电商商品图、营销AIGC素材可复用分层水印方案，叠加语义+非语义双水印，单阶攻击下至少一类水印可解码，大幅降低素材被盗用溯源失败风险

  - 评估AIGC生成素材的视觉质量不可仅依赖LPIPS指标，需补充人脸、高敏感商品区域的人工定性校验，避免上线后出现肉眼可见的失真

  - 业务侧无需过度优化单类水印性能，叠加互补方案的投入产出比远高于单方案极致优化，还可避免单方案优化带来的画质劣化问题'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有单类图像水印易被UnMarker等低成本攻击抹除，AIGC内容溯源、盗版防护需求迫切，单水印优化边际收益低且易导致画质劣化。
### 方法关键点
提出SSNSW分层水印方案，结合语义类StegaStamp、非语义类HiDDeN两种互补水印，按两种嵌入顺序先后注入图像，分别测试单阶/时序UnMarker攻击下的解码率。
### 关键结果数字
- 双水印嵌入后解码率几乎无损失，嵌入顺序对效果影响极小
- 单阶攻击下至少一类水印解码率保持较高水平：非语义攻击下StegaStamp留存率高，语义攻击下HiDDeN留存率高
- 仅连续执行两类时序攻击可同时抹除双水印，但会带来显著的画质下降
- 仅用LPIPS评估画质存在漏洞，人脸等敏感区域易出现肉眼可感知的失真

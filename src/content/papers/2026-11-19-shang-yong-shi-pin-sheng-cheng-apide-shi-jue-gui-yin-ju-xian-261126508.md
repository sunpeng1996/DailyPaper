---
title: Visual Attribution Limits and Graded Provenance Auditing in Commercial Video-Generation
  APIs
title_zh: 商用视频生成API的视觉归因局限性与分级来源审计方案
authors:
- Haocheng Mei
- Yuchuan Tian
- Yingte Shu
- Chao Xu
- Kai Han
- Hanting Chen
- Yunhe Wang
affiliations:
- Peking University
- TokenRhythm Technologies
arxiv_id: '2611.26508'
url: https://arxiv.org/abs/2611.26508
pdf_url: https://arxiv.org/pdf/2611.26508
published: '2026-11-19'
collected: '2026-11-21'
category: Other
direction: AIGC服务审计 · 视频生成API来源校验
tags:
- VideoGeneration
- Attribution
- ProvenanceAudit
- AIGCCompliance
- Cryptography
one_liner: 提出融合被动归因与密码学证明的商用视频生成API分级审计方案
practical_value: '- 若涉及AIGC API采买/代运营业务，可直接复用分级审计框架，明确可追责级和仅参考级的证据边界，降低合规纠纷成本

  - 做视频内容归因检测时，可采用将参考帧从24fps降采样到3fps的优化trick，大幅提升AUROC指标

  - 对外提供商业化AIGC API服务时，可参考BytePlus的层级签名方案，解决用户对计费层级真实性的信任问题'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
商用视频生成API按模型/层级计费，同厂商不同层级价差最高达79%，中间商存在偷换低阶模型、复用缓存片段的套利空间，行业缺乏可落地的来源校验手段。

### 方法关键点
融合被动视觉归因检测与密码学来源证明，设计三级审计机制，覆盖重编码、降分辨率、帧率变化等常见篡改场景，同时调研19个商用接口的C2PA、GB 45438元数据标准落地情况。

### 关键结果数字
原始文件的6模型归因准确率达83.9%，统一重编码后骤降至45.3%；参考帧从24fps降采样到3fps时，D3 AUROC从0.845提升至0.988；100个720p签名层级篡改案例全部被检出，诚实样本零误报；仅BytePlus支持层级签名校验，187次交付全部通过审计，重封装/重编码后签名失效。

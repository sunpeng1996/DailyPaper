---
title: 'SEEK: Secure and Efficient Encrypted Keyword Search For Privacy-Preserving
  Messaging Protocols'
title_zh: 面向隐私保护消息协议的安全高效加密关键词搜索方案SEEK
authors:
- Soumyadyuti Ghosh
- Michail Maniatakos
affiliations:
- New York University Abu Dhabi
- Center for Cyber Security
arxiv_id: '2609.18459'
url: https://arxiv.org/abs/2609.18459
pdf_url: https://arxiv.org/pdf/2609.18459
published: '2026-09-16'
collected: '2026-09-20'
category: Other
direction: 隐私保护加密关键词检索
tags:
- Homomorphic Encryption
- 2PC
- Privacy-Preserving Search
- Encrypted Messaging
one_liner: 结合同态加密与两方安全计算实现高准确率低开销的加密消息隐私保护关键词检索
practical_value: '- 端侧隐私合规的用户兴趣关键词识别、本地商品检索场景，可复用同态加密+2PC的组合架构，仅输出命中二值结果不泄露原始数据，满足合规要求

  - 长文本加密检索的最小足够重叠分片策略可直接迁移，降低端侧加密、上传开销，适配手机等弱算力终端场景

  - 单陷门大小写不敏感匹配方法可用于合规关键词审核场景，无需额外通信开销即可避免大小写变体漏判'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
端到端加密通信需平衡有害内容检测需求与用户隐私保护，现有加密关键词检索方案普遍存在计算开销高、额外信息泄露风险大的问题。
### 方法关键点
1. 融合同态加密与安全两方计算（2PC），先将消息切分为最小足够重叠的密文分片，通过加密关键词陷门完成同态关联计算
2. 采用2PC实现选择解码、盲化零检测、安全聚合逻辑，仅返回关键词是否存在的二值结果，不泄露关键词、消息内容、匹配位置/计数等额外信息
### 关键结果
- 长消息场景发送端加密、上传开销比SOTA基线低2个数量级，关联计算速度比最强分片基线快5.47倍
- 大小写变体场景下匹配准确率100%，无需额外陷门或在线通信
- 端到端原型在周级消息历史上单次搜索耗时仅1.92s

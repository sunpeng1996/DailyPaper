---
title: 'omni-macos: On-Device Omni-Modal Search on Apple Silicon'
title_zh: omni-macos：Apple Silicon 端侧全模态搜索系统
authors:
- Han Xiao
affiliations:
- Jina AI
- Elastic
arxiv_id: '2608.05543'
url: https://arxiv.org/abs/2608.05543
pdf_url: https://arxiv.org/pdf/2608.05543
published: '2026-08-06'
collected: '2026-08-07'
category: Other
direction: 端侧全模态语义搜索系统优化
tags:
- On-Device Search
- Multimodal Embedding
- Vector Index
- Apple Silicon
- Privacy Preserving
one_liner: 在Apple Silicon端侧实现全链路本地化全模态语义搜索，零数据出端，适配不同算力内存配置
practical_value: '- 端侧个人助手/私域RAG场景可复用增量索引方案：仅对编辑修改的chunk重新编码，大幅降低端侧算力开销

  - 端侧检索交互优化技巧：用户输入时向GPU传递小批量计算单元，保证检索响应时延达标

  - 统一内存资源管控思路：将用户设定的内存预算传导至所有分配器，适配不同硬件配置的端侧部署

  - 量化索引+精确重排的两级检索策略，可直接迁移到端侧低资源语义检索场景'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有全模态语义搜索全链路依赖服务端部署，用户私有文件需上传到第三方服务器，存在隐私泄露风险，端侧落地面临算力/内存受限、文件动态更新、交互时延要求高的多重瓶颈。
### 方法关键点
1. 全链路本地化部署：编码器、向量索引、存储全运行在本地Apple Silicon设备，无任何用户数据出端；
2. 增量索引优化：仅对文件编辑修改的chunk重新编码，大幅降低后台索引的算力开销；
3. 交互时延优化：用户输入时向GPU传递小批量计算单元，配合量化索引+精确重排的两级检索策略，平衡精度与响应速度；
4. 统一内存管控：将用户设定的内存预算传导至所有内存分配器，适配不同硬件配置。
### 关键结果
在5款算力跨度8倍、内存跨度32倍的Mac设备上完成全机制验证，均可稳定实现本地文件的实时全模态搜索。

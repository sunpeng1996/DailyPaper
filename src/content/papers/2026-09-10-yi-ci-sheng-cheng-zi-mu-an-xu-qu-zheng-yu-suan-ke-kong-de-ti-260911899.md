---
title: 'Caption-once, Frames-on-Demand: Visual-Need Routing for Budget-Aware Agentic
  Long Video Understanding'
title_zh: 一次生成字幕按需取帧：预算可控的智能体长视频理解视觉需求路由框架
authors:
- Weitong Cai
- Hang Zhang
- Yukai Huang
- Yiqiao Xie
- Shan Gao
- Jiankang Deng
- Songcen Xu
- Jifei Song
- Zhensong Zhang
affiliations:
- Queen Mary University of London
- Durham University
- Imperial College London
- Huawei
arxiv_id: '2609.11899'
url: https://arxiv.org/abs/2609.11899
pdf_url: https://arxiv.org/pdf/2609.11899
published: '2026-09-10'
collected: '2026-09-11'
category: Agent
direction: Agent 多模态长视频理解架构优化
tags:
- Long Video Understanding
- Edge-Cloud
- Multimodal LLM
- Visual Routing
- Budget Control
one_liner: 提出边云协同CFD框架，通过双轨文本索引加按需帧检索，以极低视觉预算实现长视频理解最优精度效率权衡
practical_value: '- 可复用「离线一次建库+在线按需检索」分层存储架构，比如电商短视频/商品素材库离线生成结构化描述缓存，线上query仅按需调取原始素材，大幅降低推理带宽与计算成本

  - 可借鉴Visual-Need Router门控设计，针对query类型（如属性查询vs时序查询）路由到不同模态处理路径，避免无差别调用高成本多模态大模型

  - 分层记忆（全局骨架+局部细节+原始素材）设计可直接迁移到电商用户行为序列建模/智能客服知识库架构，平衡全局覆盖度与局部细节精度'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有长视频理解方案要么通过压缩采样帧丢失时序结构，要么全转文本丢失细粒度视觉属性，端侧部署受算力、带宽严格约束，现有智能体方案query时反复重生成字幕的成本不可控，无法适配边云协同的低预算场景。

### 方法关键点
- 三层记忆架构：端侧离线一次生成双轨文本索引，事件级全局故事骨架（覆盖全视频时序逻辑）+ 固定长度clip级微操作日志（保存局部细节），全部缓存跨query复用，仅在文本不足时调用第三层固定容量FIFO视觉工作内存存储按需调取的关键帧
- 四类智能体分工：端侧仅运行离线字幕生成Agent，云端运行问答Agent、时序定位Agent、视觉需求路由Agent，砍掉现有方案中query时重生成字幕的指令Agent，大幅降低在线成本
- 故事优先推理循环：先用全局文本骨架尝试回答，信心不足则定位相关事件注入clip级文本再回答，仍不足则由路由模块判断是否需要调取关键帧做多模态推理，每一步都有早停机制，严格控制迭代与帧预算

### 关键实验
在Video-MME、InfiniBench长视频基准测试：对比Qwen3-VL-32B密集采样768帧的基线，CFD仅用平均5.8帧/query就达到67.5的整体精度，帧用量降低2个数量级；对比现有Agent方法VideoLucy，精度高2.8个百分点，帧用量少1个数量级；InfiniBench上时序理解任务准确率55.1，超过768帧基线的48.44。

**最值得记住的一句话**：文本不是视频的有损替代，而是长时序结构的更优载体，稀疏原始帧则是属性感知的必要补充，二者通过智能路由结合可实现极低预算下的性能最优。

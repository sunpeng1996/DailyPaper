---
title: 'AVA-Encoder: Towards Agent-Native Video Representation Learning'
title_zh: AVA-Encoder：面向Agent原生的视频表示学习框架
authors:
- Chuyue Li
- Jinpeng Yu
- Haozhe Wang
- Tian Xueyun
- Zhijing Zhang
- Bingnan Li
- Shuqi Gu
- Kan Ren
- Jiaming Liu
- Ruihua Hua
affiliations:
- Qwen Business Unit of Alibaba
- ShanghaiTech University
- The Hong Kong University of Science and Technology
- Institute of Computing Technology
- Southeast University
arxiv_id: '2608.12313'
url: https://arxiv.org/abs/2608.12313
pdf_url: https://arxiv.org/pdf/2608.12313
published: '2026-08-11'
collected: '2026-08-13'
category: Agent
direction: Agent原生视频表示 · 知识图谱自编码
tags:
- Video-Representation
- Knowledge-Graph
- TextGrad
- Auto-Encoding
- Video-Agent
one_liner: 提出基于知识图谱的Agent原生视频表示框架，通过双循环文本梯度优化，重建精度超最强基线20.7个百分点
practical_value: '- 做内容生成Agent的结构化表示可以借鉴「文本为核心的分层知识图谱+关联资产层」设计，既保留语义可解释性，又支持跨模态关联编辑，适合电商短视频/直播内容结构化解析场景

  - 不需要微调模型权重的场景可以复用「文本梯度双循环优化」思路：外层优化系统prompt（比人工写的省74%token还效果更好），内层优化单任务结构化表示，用重建反馈做自动迭代，零代码适配垂直域内容

  - 结构化表示的评估可借鉴「重建保真度+下游任务增益」的双重指标，比纯语义相似性评估更贴合生成类业务的实际效果要求，可用于短视频素材库的结构化质量验收'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前视频创作Agent无法直接从人类高质量影视内容中学习创作知识，核心痛点是缺少同时满足Agent可理解、可推理编辑、保真度足够的视频结构化表示：低阶视觉特征不可解释，纯文本描述丢失层级关系与跨模态依赖，现有知识图谱表示面向理解任务设计，缺少生成所需的细粒度信息，无法支撑高质量视频重建与创作。
### 方法关键点
- 提出以文本为核心的分层视频知识图谱表示，包含Story-Event-Shot层级节点，以及Character、Scene、Camera等状态节点，关联资产层存储生成的音视频/图像资源，通过11类带类型边保留层级、时序、语义关联，支持Agent直接查询、编辑与关联更新；
- 设计双循环文本梯度优化框架：外层数据无关伪训练循环，基于重建QA错误自动优化共享的镜头级编码prompt，加入防遗忘门避免历史效果退化；内层数据依赖知识图谱优化循环，基于重建差异自动迭代当前视频的图谱表示，加入防退化门避免非目标维度效果下降；
- 采用固定视频解码器，所有优化信号完全来自输入视频与重建视频的差异，不需要标注数据，也不需要微调大模型权重。
### 关键结果
实验覆盖6个伪训练视频+18个跨域测试视频（含动画、AI短片、经典电影），对比3个SOTA基线：
1. 整体重建精度达49.0%，比最强基线高出20.7个百分点；
2. 外层伪训练得到的prompt比人工调优版本效果高1.4个百分点，系统prompt token量减少74.3%；
3. 生成的知识图谱作为参考输入，可直接提升多个主流视频创作Agent的生成质量，整体得分平均提升0.56分（1-4分制）。
### 核心结论
结构化表示的自动优化完全可以通过文本梯度迭代完成，不需要微调模型权重，就能获得比人工调优更好、token效率更高的效果

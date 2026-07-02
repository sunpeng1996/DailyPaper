---
title: 'Goku: A Million-Scale Universal Dataset and Benchmark for Instruction-Based
  Video Editing'
title_zh: Goku：面向指令驱动视频编辑的百万级通用数据集与基准
authors:
- Sen Liang
- Cong Wang
- Zhentao Yu
- Fengbin Guan
- Zhengguang Zhou
- Teng Hu
- Youliang Zhang
- Yuan Zhou
- Xin Li
- Qinglin Lu
affiliations:
- University of Science and Technology of China
- Tencent Hunyuan
arxiv_id: '2606.30599'
url: https://arxiv.org/abs/2606.30599
pdf_url: https://arxiv.org/pdf/2606.30599
published: '2026-06-29'
collected: '2026-07-02'
category: Multimodal
direction: 多模态大模型 · 指令视频编辑数据集与基准
tags:
- Video Editing
- MLLM
- Dataset
- Benchmark
- Instruction Tuning
one_liner: 推出2M规模指令驱动视频编辑数据集、评测基准及SOTA模型，指令跟随度较开源模型高8%
practical_value: '- 可复用「复杂任务拆分为可控子问题+全流程渐进式过滤」的数据集构造pipeline，用于批量生成电商短视频编辑的训练数据

  - 解耦双分支（结构控制分支+外观渲染分支）架构可迁移到电商商品短视频AI生成/编辑场景，平衡可控性与生成效果

  - 其设计的7类编辑专项评测指标，可直接复用为短视频类内容生成/编辑系统的离线评测标准'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有指令驱动视频编辑数据集仅聚焦单任务外观编辑，无法覆盖现实场景中多任务、结构级操控等复杂创作需求，也缺乏标准化的专项评测基准。
### 方法关键点
1. 发布包含200万高质量指令对齐视频编辑对的Goku数据集，首次将任务边界从基础外观编辑扩展到主体运动控制等结构级操作
2. 设计高效数据合成管线，将复杂编辑拆解为可控子问题，配套全流程渐进式过滤系统保障数据可靠性
3. 提出Goku-Edit模型，采用MLLM作为文本编码器，解耦为掩码分支（处理结构控制）、主分支（负责外观渲染）的双分支架构
4. 配套发布Goku-Bench评测基准，包含1000个人工验证测试用例、7个编辑任务专项指标
### 关键结果
在Goku-Bench上评测，Goku-Edit的指令跟随度较其他开源模型最高提升8%

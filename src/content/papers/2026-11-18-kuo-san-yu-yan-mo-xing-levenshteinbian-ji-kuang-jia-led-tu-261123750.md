---
title: 'Beyond Replacement: Levenshtein Editing for Diffusion Language Models'
title_zh: 扩散语言模型Levenshtein编辑框架LED：突破仅替换编辑局限
authors:
- Shuaidi Wang
- Zhuocheng Gong
- Xuejie Liu
- Jianguo Li
- Yu Zhang
affiliations:
- Southern University of Science and Technology
- Inclusion AI, Ant Group
arxiv_id: '2611.23750'
url: https://arxiv.org/abs/2611.23750
pdf_url: https://arxiv.org/pdf/2611.23750
published: '2026-11-18'
collected: '2026-11-19'
category: LLM
direction: 大语言模型 · 扩散模型训练优化
tags:
- Diffusion Language Model
- Levenshtein Editing
- LCS Alignment
- Multi-stage Training
- Decoding Parallelism
one_liner: 为扩散语言模型引入插入删除编辑能力，通过无标注监督和多阶段训练提升生成质量、并行度与多样性
practical_value: '- 做电商营销文案、Query改写等生成任务时，可复用LCS在线构造编辑监督的方案，无需人工标注编辑轨迹即可训练模型的插入删除修正能力，大幅降低标注成本

  - 批量生成场景（如商品标题、种草文案批量生成）可采用LED的无置信度解码+编辑修正范式，既能提升解码并行度，还能提升大k下的Pass@k，便于从批量结果中选优

  - Agent自校正、长推理任务可复用多阶段训练思路，让模型在训练阶段接触自身的中间错误，有效缩小训练推理分布差，提升自校正成功率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有扩散语言模型（DLM）的仅替换编辑（ROE）范式只能修正单个token错误，无法高效处理缺字、多字导致的序列偏移，校正长序列偏移需要O(N)次替换，效率极低；同时ROE在中间态存在大规模错误时校正能力极差，导致无置信度解码的生成质量雪崩，而置信度引导解码又存在低熵偏见，限制了生成多样性。
### 方法关键点
- 提出LED后训练框架，扩展输出词表新增[Del][Ins]特殊token，支持Levenshtein三操作（替换/插入/删除），兼容原DLM的固定块输入接口
- 基于最长公共子序列（LCS）在线构造编辑监督信号，无需人工标注编辑轨迹即可在标准SFT数据上训练插入删除能力
- 采用推理对齐的多阶段训练，让模型接触自身早期生成的错误，缩小训练推理分布差，提升错误校正能力
### 关键实验结果
基于16B参数LLaDA2.1-Mini Base训练，对比仅ROE的基线：
1. 置信度引导解码下，12个benchmark平均得分从54.86提升到57.10，每轮前向生成token数（TPF）从6.14提升到7.05，质量和速度同时提升
2. 无置信度解码下，平均得分从27.52提升到47.19，大k下Pass@k超过无编辑的阈值解码，生成多样性显著提升
3. 块大小为128时平均得分从36.97提升到51.34，大块生成鲁棒性大幅增强
### 最值得记住的一句话
仅需给扩散语言模型新增2个特殊编辑token，用LCS自动构造监督信号做轻量后训练，就能同时实现生成质量、解码速度、多样性的三重提升

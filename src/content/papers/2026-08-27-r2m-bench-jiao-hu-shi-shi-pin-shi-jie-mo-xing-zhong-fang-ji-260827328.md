---
title: 'R2M-Bench: Evaluating Revisit Memory via Relative Consistency in Interactive
  Video World Models'
title_zh: R2M-Bench：交互式视频世界模型重访记忆的相对一致性评估基准
authors:
- Qiwen Gu
- Bingjie Gao
- Rui Chen
- Geng Li
- Jifan Li
- Qishuai Wen
- Li Niu
- Jing Tang
- Xiangxiang Chu
- Junqiao Zhao
affiliations:
- DreamX Team, Alibaba Group
- Tongji University
- Shanghai Jiao Tong University
arxiv_id: '2608.27328'
url: https://arxiv.org/abs/2608.27328
pdf_url: https://arxiv.org/pdf/2608.27328
published: '2026-08-27'
collected: '2026-08-29'
category: Eval
direction: 世界模型评估 · 记忆能力评测
tags:
- Benchmark
- World Model
- Memory Evaluation
- Relative Consistency
- Interactive Video
one_liner: 提出基于同轨迹相对校准的视频世界模型重访记忆评估基准R2M-Bench，解决绝对评分易受干扰的问题
practical_value: '- 做3D导购/具身交互Agent的场景记忆能力评估时，可复用同轨迹相对校准思路，消除渲染稳定性、运动速度对评估结果的干扰

  - 多轮搜索推荐的用户记忆点召回效果评测，可引入间隔匹配的非重访对照组计算记忆增益，避免将重复内容误判为记忆召回

  - 业务场景的相似度打分校准，可参考NMR归一化方法，用短程/基线动态范围做分母，消除不同基准的偏差'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视频世界模型重访记忆评估依赖首次访问与返回帧的绝对相似度，易受渲染稳定性、重复内容、运动失效干扰，无法区分真实记忆与中间帧变化小的假阳性结果。
### 方法关键点
提出R2M-Bench评估基准，对每个重访对引入两个同轨迹对照组：间隔匹配的非重访对（测量通用时间稳定性）、短程对（估计短时域一致性），计算两个核心指标：MemoryGain（MG，重访对相对时间基线的优势）、Normalized Memory Ratio（NMR，用短程对到基线的动态范围归一化优势）。基准含100个参考场景+3条往返轨迹共300个实例，覆盖外观保真、场景/物体身份、局部几何、持久状态4个评估维度。
### 关键结果
7个动作条件视频世界模型测试中，整体NMR与人类一致性判断的斯皮尔曼相关系数ρ=0.547；与生成运动的组内相关仅0.072，远低于原始重访相似度的0.207，大幅降低慢动作捷径干扰；DreamX-World-Memo取得最高整体NMR。

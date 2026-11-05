---
title: 'Transforming Integer Grids to Spatial Intuition: Perception, Not Planning,
  Governs ARC-AGI-3'
title_zh: 将整数网格转换为空间直觉：感知而非规划主导ARC-AGI-3基准
authors:
- Harsidak Singh Banwait
affiliations:
- Independent Researcher
arxiv_id: '2611.06793'
url: https://arxiv.org/abs/2611.06793
pdf_url: https://arxiv.org/pdf/2611.06793
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: 交互式推理Agent · 空间感知优化
tags:
- Agent
- Spatial Perception
- ARC-AGI-3
- KV Cache
- CodeAct
one_liner: 提出开源Sarbloh Agent架构，通过零参数空间感知引擎大幅提升ARC-AGI-3基准推理效率
practical_value: '- 可复用Measured–Guessed Rule到电商导购/推荐/广告Agent场景：将可确定性计算的事实（如商品属性、用户历史行为、页面空间布局）直接结构化输入LLM，将需要验证的假设（如用户潜在兴趣、转化触发点）标注为猜测并配套1次低代价交互验证，避免无目的探索浪费交互机会

  - 基础特征提取优先用零参数确定性代码而非大模型推理：比如推荐场景下的商品关联性、用户行为序列的统计特征、广告位的空间属性等提前用规则计算，无需让LLM从原始日志/raw像素中重构，可降低80%+
  token消耗，同时减少感知错误

  - 工程上可复用append-only KV cache + 确定性上下文清理策略：多轮交互Agent不使用LLM生成上下文摘要（易产生幻觉且消耗算力），上下文溢出时直接删除最早的完整交互轮次，可实现98%+前缀缓存命中率，大幅降低推理成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
ARC-AGI-3基准采用Relative Human Action Efficiency（RHAE）指标评估Agent在无指令视觉游戏中的样本高效推理能力，对多余探索动作做二次惩罚。现有前沿推理模型直接处理原始整数网格输入时，序列化操作会破坏空间拓扑结构，引发感知错误诱导，模型需浪费数百次动作重构基础边界、对称性等空间特征，探索成本极高，推理效率远低于人类水平。
### 方法关键点
1. 定义**Measured–Guessed Rule**：确定性可计算的几何不变量（可达性、封闭性、D4对称、中点约束等）作为事实直接输出，需验证的功能假设（如可交互物体角色）标注为猜测并配套单动作验证方案，避免错误假设导致的高代价探索
2. 零参数O(HW)感知引擎，单CPU核35ms/帧完成原始网格到带时序跟踪的对象清单、几何简报、标注空间画布的转换，token消耗降低89.4%
3. 代码即动作的speculative运行时，Agent直接合成算法假设而非低阶动作原语，通过`await play()`接口执行多步路径，出现感知预测偏差立即终止
4. 仅追加式KV cache设计，缓存命中率达98.4%，采用确定性上下文清理（溢出时直接删除最早的完整交互轮次）代替LLM摘要，避免幻觉同时降低算力消耗
### 关键结果
在官方9小时单NVIDIA RTX PRO 6000 GPU约束下，Sarbloh在ARC-AGI-3隐藏测试集得分16.53，较首个里程碑优胜者提升13.7倍；25个公开环境上平均效率72.5%，优于GPT-6.1、Claude Opus 5等5个前沿API基线；几何不变量在23个未见过的游戏上空间准确率100%，单帧功能猜测准确率仅6%~50%，验证了主动假设验证的必要性。
**最值得记住的结论**：交互式推理的核心瓶颈通常不是规划能力不足，而是感知层的错误诱导，确定性先验提取+低代价假设验证的组合，效率远高于纯大模型端到端推理。
